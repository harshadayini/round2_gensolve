import re
import numpy as np
import matplotlib.pyplot as plt
import svgwrite
from scipy.ndimage import gaussian_filter1d
import csv
import os

def clean_data_with_regex(file_path):
    cleaned_data = []
    with open(file_path, 'r') as file:
        for line in file:

            numbers = re.findall(r'-?\d+\.\d+e[+-]?\d+|\d+\.\d+|\d+', line)

            cleaned_data.append([float(num) for num in numbers])
    return np.array(cleaned_data)

def smooth_outer_box(data, sigma=10):  
    x_coords = data[:, 2]
    y_coords = data[:, 3]

    x_smoothed = gaussian_filter1d(x_coords, sigma)
    y_smoothed = gaussian_filter1d(y_coords, sigma)

    smoothed_box = np.hstack((data[:, :2], x_smoothed.reshape(-1, 1), y_smoothed.reshape(-1, 1)))

    return smoothed_box

def identify_outermost_rectangle(data):

    max_x, min_x = np.max(data[:, 2]), np.min(data[:, 2])
    max_y, min_y = np.max(data[:, 3]), np.min(data[:, 3])

    outermost_rect = data[
        (data[:, 2] == max_x) | (data[:, 2] == min_x) | 
        (data[:, 3] == max_y) | (data[:, 3] == min_y)
    ]

    return outermost_rect

def correct_data(data, sigma=10):  
    corrected_data = []

    outermost_rectangle = identify_outermost_rectangle(data)

    for identifier in np.unique(data[:, 0]):
        shape_data = data[data[:, 0] == identifier]
        if identifier == outermost_rectangle[0, 0]:  
            corrected_shape_data = smooth_outer_box(shape_data, sigma=sigma)
        else:
            corrected_shape_data = shape_data
        corrected_data.append(corrected_shape_data)

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

def save_as_svg(data, output_path):
    dwg = svgwrite.Drawing(output_path, profile='tiny')
    for identifier in np.unique(data[:, 0]):
        shape_data = data[data[:, 0] == identifier]
        points = [(x, y) for x, y in zip(shape_data[:, 2], shape_data[:, 3])]
        dwg.add(dwg.polyline(points, stroke='black', fill='none'))
    dwg.save()

def save_as_csv(data, output_path):
    with open(output_path, mode='w', newline='') as file:
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

data = clean_data_with_regex(file_path)

plot_data(data, title="Original Shape Data", color='red')

corrected_data = correct_data(data, sigma=10)  

plot_data(corrected_data, title="Corrected Shape Data", color='green')

save_as_svg(corrected_data, output_svg_path)
print(f"Corrected shape saved to {output_svg_path}")

save_as_csv(corrected_data, output_csv_path)
print(f"Final output saved as CSV to {output_csv_path}")