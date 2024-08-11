import numpy as np
import pandas as pd

def generate_densified_circle_csv(radius=1, num_points=100, center=(0, 0), filename="densified_circle.csv"):
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x_values = center[0] + radius * np.cos(angles)
    y_values = center[1] + radius * np.sin(angles)

    data = {
        "ContourID": np.ones(num_points, dtype=int),
        "SegmentID": np.ones(num_points, dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")
generate_densified_circle_csv(radius=100, num_points=100, center=(100, 100), filename="densified_circle.csv")

def generate_densified_octagon_csv(radius=1, center=(0, 0), num_points_per_side=10, filename="densified_octagon.csv"):
    sides = 8
    angles = np.linspace(0, 2 * np.pi, sides + 1, endpoint=True)  # Closing the octagon
    x_values = []
    y_values = []
    
    for i in range(sides):
        start_angle = angles[i]
        end_angle = angles[i + 1]
        segment_angles = np.linspace(start_angle, end_angle, num_points_per_side, endpoint=False)
        x_values.extend(center[0] + radius * np.cos(segment_angles))
        y_values.extend(center[1] + radius * np.sin(segment_angles))
    
    x_values.append(x_values[0])  # Close the shape
    y_values.append(y_values[0])  # Close the shape

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")
generate_densified_octagon_csv(radius=100, center=(100, 100), num_points_per_side=10, filename="densified_octagon.csv")


def generate_hexagon_csv(radius=1, center=(0, 0), num_points_per_side=10, filename="hexagon.csv"):
    sides = 6
    angles = np.linspace(0, 2 * np.pi, sides + 1, endpoint=True)  # Closing the hexagon
    x_values = []
    y_values = []

    for i in range(sides):
        start_angle = angles[i]
        end_angle = angles[i + 1]
        segment_angles = np.linspace(start_angle, end_angle, num_points_per_side, endpoint=False)
        x_values.extend(center[0] + radius * np.cos(segment_angles))
        y_values.extend(center[1] + radius * np.sin(segment_angles))

    x_values.append(x_values[0])  # Close the shape
    y_values.append(y_values[0])  # Close the shape

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")
generate_hexagon_csv(radius=100, center=(100, 100), num_points_per_side=10, filename="hexagon.csv")


def generate_heptagon_csv(radius=1, center=(0, 0), num_points_per_side=10, filename="heptagon.csv"):
    sides = 7
    angles = np.linspace(0, 2 * np.pi, sides + 1, endpoint=True)  # Closing the heptagon
    x_values = []
    y_values = []

    for i in range(sides):
        start_angle = angles[i]
        end_angle = angles[i + 1]
        segment_angles = np.linspace(start_angle, end_angle, num_points_per_side, endpoint=False)
        x_values.extend(center[0] + radius * np.cos(segment_angles))
        y_values.extend(center[1] + radius * np.sin(segment_angles))

    x_values.append(x_values[0])  # Close the shape
    y_values.append(y_values[0])  # Close the shape

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")
generate_heptagon_csv(radius=100, center=(100, 100), num_points_per_side=10, filename="heptagon.csv")

def generate_pentagon_csv(radius=1, center=(0, 0), num_points_per_side=10, filename="pentagon.csv"):
    sides = 5
    angles = np.linspace(0, 2 * np.pi, sides + 1, endpoint=True)  # Closing the pentagon
    x_values = []
    y_values = []

    for i in range(sides):
        start_angle = angles[i]
        end_angle = angles[i + 1]
        segment_angles = np.linspace(start_angle, end_angle, num_points_per_side, endpoint=False)
        x_values.extend(center[0] + radius * np.cos(segment_angles))
        y_values.extend(center[1] + radius * np.sin(segment_angles))

    x_values.append(x_values[0])  # Close the shape
    y_values.append(y_values[0])  # Close the shape

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")
generate_pentagon_csv(radius=100, center=(100, 100), num_points_per_side=10, filename="pentagon.csv")


def generate_nonagon_csv(radius=1, center=(0, 0), num_points_per_side=10, filename="nonagon.csv"):
    sides = 9
    angles = np.linspace(0, 2 * np.pi, sides + 1, endpoint=True)  # Closing the nonagon
    x_values = []
    y_values = []

    for i in range(sides):
        start_angle = angles[i]
        end_angle = angles[i + 1]
        segment_angles = np.linspace(start_angle, end_angle, num_points_per_side, endpoint=False)
        x_values.extend(center[0] + radius * np.cos(segment_angles))
        y_values.extend(center[1] + radius * np.sin(segment_angles))

    x_values.append(x_values[0])  # Close the shape
    y_values.append(y_values[0])  # Close the shape

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")
generate_nonagon_csv(radius=100, center=(100, 100), num_points_per_side=10, filename="nonagon.csv")


def generate_decagon_csv(radius=1, center=(0, 0), num_points_per_side=10, filename="decagon.csv"):
    sides = 10
    angles = np.linspace(0, 2 * np.pi, sides + 1, endpoint=True)  # Closing the decagon
    x_values = []
    y_values = []

    for i in range(sides):
        start_angle = angles[i]
        end_angle = angles[i + 1]
        segment_angles = np.linspace(start_angle, end_angle, num_points_per_side, endpoint=False)
        x_values.extend(center[0] + radius * np.cos(segment_angles))
        y_values.extend(center[1] + radius * np.sin(segment_angles))

    x_values.append(x_values[0])  # Close the shape
    y_values.append(y_values[0])  # Close the shape

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")
generate_decagon_csv(radius=100, center=(100, 100), num_points_per_side=10, filename="decagon.csv")


def generate_triangle_csv(radius=1, center=(0, 0), num_points_per_side=10, filename="triangle.csv"):
    sides = 3
    angles = np.linspace(0, 2 * np.pi, sides + 1, endpoint=True)  # Closing the triangle
    x_values = []
    y_values = []

    for i in range(sides):
        start_angle = angles[i]
        end_angle = angles[i + 1]
        segment_angles = np.linspace(start_angle, end_angle, num_points_per_side, endpoint=False)
        x_values.extend(center[0] + radius * np.cos(segment_angles))
        y_values.extend(center[1] + radius * np.sin(segment_angles))

    x_values.append(x_values[0])  # Close the shape
    y_values.append(y_values[0])  # Close the shape

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")

generate_triangle_csv(radius=100, center=(100, 100), num_points_per_side=10, filename="triangle.csv")

def generate_square_csv(side_length=200, center=(0, 0), num_points_per_side=25, filename="square.csv"):
    half_side = side_length / 2

    x_values = []
    y_values = []

    # Bottom edge (left to right)
    x_values.extend(np.linspace(center[0] - half_side, center[0] + half_side, num_points_per_side, endpoint=False))
    y_values.extend([center[1] - half_side] * num_points_per_side)

    # Right edge (bottom to top)
    x_values.extend([center[0] + half_side] * num_points_per_side)
    y_values.extend(np.linspace(center[1] - half_side, center[1] + half_side, num_points_per_side, endpoint=False))

    # Top edge (right to left)
    x_values.extend(np.linspace(center[0] + half_side, center[0] - half_side, num_points_per_side, endpoint=False))
    y_values.extend([center[1] + half_side] * num_points_per_side)

    # Left edge (top to bottom)
    x_values.extend([center[0] - half_side] * num_points_per_side)
    y_values.extend(np.linspace(center[1] + half_side, center[1] - half_side, num_points_per_side, endpoint=False))

    # Close the shape by adding the first point again
    x_values.append(x_values[0])
    y_values.append(y_values[0])

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")

generate_square_csv(side_length=200, center=(100, 100), num_points_per_side=25, filename="square.csv")

def generate_straight_line_csv(start=(0, 0), end=(100, 100), num_points=100, filename="straight_line.csv"):
    x_values = np.linspace(start[0], end[0], num_points)
    y_values = np.linspace(start[1], end[1], num_points)

    data = {
        "ContourID": np.ones(num_points, dtype=int),
        "SegmentID": np.ones(num_points, dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")

generate_straight_line_csv(start=(50, 50), end=(150, 150), num_points=100, filename="straight_line.csv")

def generate_star_csv(points=5, outer_radius=100, inner_radius=50, center=(100, 100), filename="star.csv"):
    angles = np.linspace(0, 2 * np.pi, 2 * points + 1, endpoint=True)
    radii = np.array([outer_radius, inner_radius] * points + [outer_radius])

    x_values = center[0] + radii * np.cos(angles)
    y_values = center[1] + radii * np.sin(angles)

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")

generate_star_csv(points=5, outer_radius=100, inner_radius=50, center=(100, 100), filename="star.csv")

def generate_rectangle_csv(width=200, height=100, center=(100, 100), num_points_per_side=25, filename="rectangle.csv"):
    half_width = width / 2
    half_height = height / 2

    x_values = []
    y_values = []

    # Bottom edge (left to right)
    x_values.extend(np.linspace(center[0] - half_width, center[0] + half_width, num_points_per_side, endpoint=False))
    y_values.extend([center[1] - half_height] * num_points_per_side)

    # Right edge (bottom to top)
    x_values.extend([center[0] + half_width] * num_points_per_side)
    y_values.extend(np.linspace(center[1] - half_height, center[1] + half_height, num_points_per_side, endpoint=False))

    # Top edge (right to left)
    x_values.extend(np.linspace(center[0] + half_width, center[0] - half_width, num_points_per_side, endpoint=False))
    y_values.extend([center[1] + half_height] * num_points_per_side)

    # Left edge (top to bottom)
    x_values.extend([center[0] - half_width] * num_points_per_side)
    y_values.extend(np.linspace(center[1] + half_height, center[1] - half_height, num_points_per_side, endpoint=False))

    # Close the shape by adding the first point again
    x_values.append(x_values[0])
    y_values.append(y_values[0])

    data = {
        "ContourID": np.ones(len(x_values), dtype=int),
        "SegmentID": np.ones(len(x_values), dtype=int),
        "X": np.round(x_values, 6),
        "Y": np.round(y_values, 6)
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as {filename}")

generate_rectangle_csv(width=200, height=100, center=(100, 100), num_points_per_side=25, filename="rectangle.csv")