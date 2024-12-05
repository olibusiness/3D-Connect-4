import pygame
import graphics
import grid
import logic 


pygame.init()

Width, Height = 800, 600

# Create a screen/window
screen = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
pygame.display.set_caption("3D Connect 4")

# Colours
BLACK = (0, 0, 0)
WOOD_LIGHT = (229, 194, 152)
ORANGE = (255, 211, 61)
BROWN = (204,102,0)
TURN=0

SPHERE_RADIUS = 20

def main():
    global TURN
    clock = pygame.time.Clock()
    points = graphics.generate_grid()
    points = graphics.rotate_y_90(points)
    logical_grid = grid.create_rest_grid()  # Initialize the logical 3D grid
    colors = [WOOD_LIGHT] * len(points)  # Initial color of spheres
    angle_x = 0
    angle_y = 0

    # Map points to grid positions
    point_to_grid_map = {}
    grid_size = 4
    index = 0
    for z in range(grid_size):
        for y in range(grid_size):
            for x in range(grid_size):
                point_to_grid_map[index] = (z, y, x)  # Maps 1D index to (z, y, x)
                index += 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Key inputs for rotating the camera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            angle_y += 0.05  # Rotate left (Y-axis)
        if keys[pygame.K_RIGHT]:
            angle_y -= 0.05  # Rotate right (Y-axis)
        if keys[pygame.K_UP]:
            angle_x += 0.05  # Rotate up (X-axis)
        if keys[pygame.K_DOWN]:
            angle_x -= 0.05  # Rotate down (X-axis)

        # Clear screen
        screen.fill(BLACK)

        # Rotate points and draw them
        rotated_points = [graphics.rotate_x(graphics.rotate_y(point, angle_y), angle_x) for point in points]
        projected_points = [graphics.project(point) for point in rotated_points]

        for i, p in enumerate(projected_points):
            pygame.draw.circle(screen, colors[i], p, SPHERE_RADIUS)


        # Check for mouse clicks
        if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, p in enumerate(projected_points):
                px, py = p
                distance = ((mouse_x - px) ** 2 + (mouse_y - py) ** 2) ** 0.5
                if distance <= SPHERE_RADIUS:
                    if colors[i] == WOOD_LIGHT:  # Only allow updating if unclicked
                        if logic.who_move(TURN) == True:
                            TURN = TURN+1
                            colors[i] = ORANGE  # Change color to red
                            layer, row, col = point_to_grid_map[i]  # Get logical grid position
                            grid.update_grid(logical_grid, layer, row, col, 1)  # Update grid
                            if logic.check_win(logical_grid) == True:
                                print("Winner White")
                                running = False
                        else:
                            TURN = TURN+1
                            colors[i] = BROWN  # Change color to red
                            layer, row, col = point_to_grid_map[i]  # Get logical grid position
                            grid.update_grid(logical_grid, layer, row, col, 2)  # Update grid
                            if logic.check_win(logical_grid) == True:
                                print("Winner Brown")
                                running = False

                        print(f"Updated grid position: ({layer}, {row}, {col})")
        if grid.grid_status(logical_grid) == True:
            print("Board full, game over")
            running = False
        else: pass

        # Update display
        pygame.display.flip()
        clock.tick(30)
    # Make it ask if you want to view board otherwise quite
    pygame.quit()

if __name__ == "__main__":
    main()