import pygame
import graphics

pygame.init()

Width,Height = 800, 600

# Create a screen/window
screen = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
pygame.display.set_caption("3D Connect 4")

# Colours
BLACK = (0, 0, 0)
WOOD_LIGHT = (229, 194, 152)

SPHERE_RADIUS = 20

def main():
    clock = pygame.time.Clock()
    points = graphics.generate_grid()
    angle_x = 0
    angle_y = 0

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

        for p in projected_points:
            pygame.draw.circle(screen, WOOD_LIGHT, p, SPHERE_RADIUS)

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()