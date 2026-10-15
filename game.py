import pygame
import sys
from puzzle.board import Board
TILE_SIZE = 100
GAP = 4
WINDOW_SIZE = TILE_SIZE *4

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("fifteen-puzzle")
    font = pygame.font.SysFont(None, 50)

    clock = pygame.time.Clock()

    board = Board()
    board.shuffle()
    while True:
        screen.fill((0,0,0))

        for i in range(16):
            number = board.tiles[i]
            if number != 0:
                text = font.render(str(number), True, (0, 0, 0))
                row = i // 4
                column = i % 4
                rect = pygame.Rect(TILE_SIZE*column+GAP//2,TILE_SIZE*row+GAP//2, TILE_SIZE-GAP, TILE_SIZE-GAP)
                pygame.draw.rect(screen, (255,255,255), rect)

                text_rect = text.get_rect(center = rect.center)
                screen.blit(text, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    row_select = event.pos[1] // TILE_SIZE
                    column_select = event.pos[0] // TILE_SIZE
                    index_select = 4 * row_select + column_select
                    board.move(index_select)
        clock.tick(60)


if __name__ == "__main__":
    main()