import pygame
import graphics
import grid
import logic 
import time


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
white = (255, 255, 255)
black = (0, 0, 0)
TURN=0
mediumFont = pygame.font.SysFont("Arial", 28)
largeFont = pygame.font.SysFont("Arial", 40)
moveFont = pygame.font.SysFont("Arial", 60)

SPHERE_RADIUS = 20

def main():
    global TURN
    clock = pygame.time.Clock()
    points = graphics.generate_grid()
    points = graphics.rotate_points(points)
    logical_grid = grid.create_rest_grid()  # Initialize logical 3D grid
    colors = [(0, 0, 0, 0)] * len(points)  # Fully transparent by default
    angle_x = 0
    angle_y = 0
    user = None

    # Map points to grid positions
    point_to_grid_map = {}
    grid_size = 4
    index = 0
    for z in range(grid_size):
        for y in range(grid_size):
            for x in range(grid_size):
                point_to_grid_map[index] = (z, y, x)
                index += 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Start screen
        if user == None: 
            # Draw title

            title = largeFont.render("Play 3D Connect 4", True, white)
            titleRect = title.get_rect()
            titleRect.center = ((Width / 2), 50)
            screen.blit(title, titleRect)

            # Draw buttons
            playXButton = pygame.Rect((Width / 8), (Height / 2), Width / 4, 50)
            playX = mediumFont.render("Single Player", True, black)
            playXRect = playX.get_rect()
            playXRect.center = playXButton.center
            pygame.draw.rect(screen, white, playXButton)
            screen.blit(playX, playXRect)

            playOButton = pygame.Rect(5 * (Width / 8), (Height / 2), Width / 4, 50)
            playO = mediumFont.render("Two Player", True, black)
            playORect = playO.get_rect()
            playORect.center = playOButton.center
            pygame.draw.rect(screen, white, playOButton)
            screen.blit(playO, playORect)

            # Check if button is clicked
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if playXButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = True # single player
                    print(user)
                elif playOButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = False # Two player
                    print(user)
        
        else:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                angle_y += 0.05
            if keys[pygame.K_RIGHT]:
                angle_y -= 0.05
            if keys[pygame.K_UP]:
                angle_x += 0.05
            if keys[pygame.K_DOWN]:
                angle_x -= 0.05

            screen.fill(BLACK)

            rotated_points = [graphics.rotate_x(graphics.rotate_y(point, angle_y), angle_x) for point in points]
            projected_points = [graphics.project(point) for point in rotated_points]

            for i, p in enumerate(projected_points):
                layer, row, col = point_to_grid_map[i]
                sphere_surface = pygame.Surface((SPHERE_RADIUS * 2, SPHERE_RADIUS * 2), pygame.SRCALPHA)
                
                # Only show legal moves and existing player moves
                if logic.legal_move(logical_grid, layer, row, col):
                    color = (*WOOD_LIGHT, 60)  # Semi-transparent WOOD_LIGHT for legal moves
                else:
                    color = colors[i]  # Keep existing color for player moves, else fully transparent

                pygame.draw.circle(sphere_surface, color, (SPHERE_RADIUS, SPHERE_RADIUS), SPHERE_RADIUS)
                screen.blit(sphere_surface, (p[0] - SPHERE_RADIUS, p[1] - SPHERE_RADIUS))

            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                min_distance = float('inf')
                closest_sphere = None
                for i, p in enumerate(projected_points):
                    px, py = p
                    distance = ((mouse_x - px) ** 2 + (mouse_y - py) ** 2) ** 0.5
                    if distance <= SPHERE_RADIUS and distance < min_distance:
                        min_distance = distance
                        closest_sphere = i

                if user == False:        
                    if closest_sphere is not None:
                        i = closest_sphere
                        layer, row, col = point_to_grid_map[i]
                        if logic.legal_move(logical_grid, layer, row, col):
                            if logic.who_move(TURN):
                                TURN += 1
                                colors[i] = ORANGE  # Change color to orange for player 1
                                grid.update_grid(logical_grid, layer, row, col, 1)
                                if logic.check_win(logical_grid):
                                    print("Winner White")
                                    running = False
                            else:
                                TURN += 1
                                colors[i] = BROWN  # Change color to brown for player 2
                                grid.update_grid(logical_grid, layer, row, col, 2)
                                if logic.check_win(logical_grid):
                                    print("Winner Brown")
                                    running = False
                else:
                    print("Work in progress")
                    running = False


            if grid.grid_status(logical_grid):
                print("Board full, game over")
                running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()