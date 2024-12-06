import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600



# Grid settings
GRID_SIZE = 4
CELL_SIZE = 50  # Distance between points
SPHERE_RADIUS = 20

# Projection settings
FOV = 500  # Field of view
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# Rotate around the X-axis
def rotate_x(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    y_new = cos_a * y - sin_a * z
    z_new = sin_a * y + cos_a * z
    return (x, y_new, z_new)

# Rotate around the Y-axis
def rotate_y(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    x_new = cos_a * x + sin_a * z
    z_new = -sin_a * x + cos_a * z
    return (x_new, y, z_new)

# 3D to 2D projection
def project(point):
    x, y, z = point
    factor = FOV / (FOV + z)
    x_2d = x * factor + CENTER_X
    y_2d = y * factor + CENTER_Y
    return (int(x_2d), int(y_2d))

# Generate grid points
def generate_grid():
    points = []
    offset = (GRID_SIZE - 1) * CELL_SIZE // 2
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(GRID_SIZE):
                points.append((x * CELL_SIZE - offset, y * CELL_SIZE - offset, z * CELL_SIZE - offset))
    return points

def rotate_points(points):
    rotated_points = []
    for x, y, z in points:
        new_x = z
        new_y = -x
        new_z = y
        rotated_points.append((new_x, new_y, new_z))
    return rotated_points