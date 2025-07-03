import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
GRID_SIZE = 4
TILE_SIZE = SCREEN_WIDTH // GRID_SIZE
MARGIN = 10
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
TEXT_COLOR = (119, 110, 101)
FONT = pygame.font.Font(None, 40)
BIG_FONT = pygame.font.Font(None, 60)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2048")

# Functions for game mechanics
def init_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

def add_new_tile(grid):
    empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        grid[r][c] = 2 if random.random() < 0.9 else 4

def slide_row_left(row):
    non_zero = [num for num in row if num != 0]
    new_row = []
    skip = False
    for i in range(len(non_zero)):
        if skip:
            skip = False
            continue
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            new_row.append(non_zero[i] * 2)
            skip = True
        else:
            new_row.append(non_zero[i])
    return new_row + [0] * (GRID_SIZE - len(new_row))

def slide_left(grid):
    new_grid = [slide_row_left(row) for row in grid]
    return new_grid

def rotate_grid(grid):
    return [list(row) for row in zip(*grid[::-1])]

def can_move(grid):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == 0:
                return True
            if r + 1 < GRID_SIZE and grid[r][c] == grid[r + 1][c]:
                return True
            if c + 1 < GRID_SIZE and grid[r][c] == grid[r][c + 1]:
                return True
    return False

# Drawing functions
def draw_grid(grid, score):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (250, 248, 239), (0, 0, SCREEN_WIDTH, TILE_SIZE), border_radius=10)
    score_text = FONT.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 10))
    
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = grid[r][c]
            color = TILE_COLORS.get(value, (60, 58, 50))
            x, y = c * TILE_SIZE + MARGIN, r * TILE_SIZE + TILE_SIZE + MARGIN
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE - 2 * MARGIN, TILE_SIZE - 2 * MARGIN), border_radius=8)
            if value > 0:
                text = BIG_FONT if value > 100 else FONT
                label = text.render(str(value), True, TEXT_COLOR if value <= 4 else (255, 255, 255))
                text_rect = label.get_rect(center=(x + (TILE_SIZE - 2 * MARGIN) // 2, y + (TILE_SIZE - 2 * MARGIN) // 2))
                screen.blit(label, text_rect)

# Main loop
def main():
    grid = init_grid()
    score = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    new_grid = slide_left(grid)
                    if new_grid != grid:
                        grid = new_grid
                        moved = True
                elif event.key == pygame.K_RIGHT:
                    grid = rotate_grid(rotate_grid(grid))
                    new_grid = slide_left(grid)
                    if new_grid != grid:
                        grid = new_grid
                        moved = True
                    grid = rotate_grid(rotate_grid(grid))
                elif event.key == pygame.K_UP:
                    grid = rotate_grid(rotate_grid(rotate_grid(grid)))
                    new_grid = slide_left(grid)
                    if new_grid != grid:
                        grid = new_grid
                        moved = True
                    grid = rotate_grid(grid)
                elif event.key == pygame.K_DOWN:
                    grid = rotate_grid(grid)
                    new_grid = slide_left(grid)
                    if new_grid != grid:
                        grid = new_grid
                        moved = True
                    grid = rotate_grid(rotate_grid(rotate_grid(grid)))
                
                if moved:
                    add_new_tile(grid)
                    score += sum(sum(row) for row in grid)
                
                if not can_move(grid):
                    print("Game Over!")
                    running = False

        draw_grid(grid, score)
        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()
    sys.exit()

main()