import pygame
import sys

COLORS = {
    "water": (0, 0, 255),
    "grass": (34, 139, 34),
    "mountain": (139, 137, 137),
    "unknown": (255, 0, 255)
}

def render(grid, cell_size=20, title="Procedural Map (R = regen)"):
    rows = len(grid)
    cols = len(grid[0]) if rows>0 else 0

    pygame.init()
    screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # indica regenerar para o main
                    pygame.display.quit()
                    return "regen"

        screen.fill((0, 0, 0))
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                color = COLORS.get(cell, (255,255,255))
                pygame.draw.rect(screen, color, (j*cell_size, i*cell_size, cell_size, cell_size))
        pygame.display.flip()
        clock.tick(60)