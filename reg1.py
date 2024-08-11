import numpy as np
import matplotlib.pyplot as plt
import drawsvg as draw
from joblib import Parallel, delayed
import os
import csv

def clean_data_with_numpy(file_path):
    return np.genfromtxt(file_path, delimiter=',', skip_header=0)

def find_bounding_box_corners(data):
    min_coords = np.min(data[:, 2:4], axis=0)
    max_coords = np.max(data[:, 2:4], axis=0)
    return min_coords[0], min_coords[1], max_coords[0], max_coords[1]

def correct_outer_box(data):
    min_x, min_y, max_x, max_y = find_bounding_box_corners(data)

    corrected_box = np.array([
        [min_x, min_y],
        [max_x, min_y],
        [max_x, max_y],
        [min_x, max_y],
        [min_x, min_y]  
    ])

    repeated_id_data = np.repeat(data[:1, :2], corrected_box.shape[0], axis=0)
    corrected_outer_box = np.hstack((repeated_id_data, corrected_box))

    return corrected_outer_box

def detect_irregular_box(points, aspect_ratio_threshold=0.2, edge_deviation_threshold=2.0):
    if points.shape[0] < 4:
        return False

    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)

    width = max_x - min_x
    height = max_y - min_y
    aspect_ratio = width / height

    if np.abs(aspect_ratio - 1) > aspect_ratio_threshold:
        return True

    edge_deviations = np.array([
        np.std(points[points[:, 0] == min_x][:, 1]),  
        np.std(points[points[:, 0] == max_x][:, 1]),  
        np.std(points[points[:, 1] == min_y][:, 0]),  
        np.std(points[points[:, 1] == max_y][:, 0])  
    ])

    return np.any(edge_deviations > edge_deviation_threshold)

def process_shape(identifier, data):
    shape_data = data[data[:, 0] == identifier][:, 2:4]
    if detect_irregular_box(shape_data):
        print(f"Detected irregular box shape for identifier {identifier}. Correcting it.")
        return correct_outer_box(data[data[:, 0] == identifier])
    return data[data[:, 0] == identifier]

def correct_data(data):
    identifiers = np.unique(data[:, 0])
    corrected_data = Parallel(n_jobs=-1)(delayed(process_shape)(identifier, data) for identifier in identifiers)
    return np.vstack(corrected_data)

def plot_data(data, title="Shape Data", color='blue'):
    plt.figure(figsize=(8, 8))
    unique_ids = np.unique(data[:, 0])
    for uid in unique_ids:
        shape_data = data[data[:, 0] == uid]
        plt.plot(shape_data[:, 2], shape_data[:, 3], color=color)
    plt.title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def visualize_with_drawsvg(data, output_svg_path):
    d = draw.Drawing(300, 300, origin='center')

    for identifier in np.unique(data[:, 0]):
        shape_data = data[data[:, 0] == identifier]
        d.append(draw.Lines(
            *shape_data[:, 2:4].flatten(),  
            close=True, fill='none', stroke='black'
        ))

    d.save_svg(output_svg_path)
    print(f"Corrected shape saved to {output_svg_path}")
    return d

def save_as_csv(data, output_csv_path):
    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Contour ID 1", "Contour ID 2", "X", "Y"])
        for row in data:
            writer.writerow(row)

file_path = input("Enter the path to the input CSV file: ")

output_directory = input("Enter the directory where you want to save the output files: ")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

output_svg_path = os.path.join(output_directory, "output_corrected_shape.svg")
output_csv_path = os.path.join(output_directory, "final_output_regularized.csv")

data = clean_data_with_numpy(file_path)

plot_data(data, title="Original Shape Data", color='red')

corrected_data = correct_data(data)

plot_data(corrected_data, title="Corrected Shape Data", color='green')

visualize_with_drawsvg(corrected_data, output_svg_path)

save_as_csv(corrected_data, output_csv_path)
print(f"Final output saved as CSV to {output_csv_path}")