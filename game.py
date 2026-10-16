import pygame
import sys
from puzzle.board import Board
TILE_SIZE = 100
GAP = 4
HEADER = 60
WINDOW_SIZE = TILE_SIZE *4

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE+HEADER))
    pygame.display.set_caption("fifteen-puzzle")
    font = pygame.font.SysFont(None, 50)

    clock = pygame.time.Clock()

    board = Board()
    board.shuffle(5)
    moves = 0
    while True:
        screen.fill((0,0,0))

        for i in range(16):
            number = board.tiles[i]
            if number != 0:
                text = font.render(str(number), True, (0, 0, 0))
                row = i // 4
                column = i % 4
                rect = pygame.Rect(TILE_SIZE*column+GAP//2,TILE_SIZE*row+GAP//2+HEADER, TILE_SIZE-GAP, TILE_SIZE-GAP)
                pygame.draw.rect(screen, (255,255,255), rect)

                text_rect = text.get_rect(center = rect.center)
                screen.blit(text, text_rect)

        text_moves = font.render(f"moves:{moves}", True, (255, 255, 255))
        screen.blit(text_moves, (0,0))

        if board.is_solved():
            text_clear = font.render("CLEAR!", True, (255, 0, 0))
            text_clear_rect = text_clear.get_rect(center = (WINDOW_SIZE//2,HEADER+WINDOW_SIZE//2))
            screen.blit(text_clear, text_clear_rect)
    
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[1] >= HEADER:
                        row_select = (event.pos[1]-HEADER) // TILE_SIZE
                        column_select = event.pos[0] // TILE_SIZE
                        index_select = 4 * row_select + column_select
                        if board.move(index_select):
                            moves += 1
        clock.tick(60)


if __name__ == "__main__":
    main()