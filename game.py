import pygame
import sys
from puzzle.board import Board
from pathlib import Path
ASSETS = Path(__file__).parent/"assets"
TILE_SIZE = 100
GAP = 4
HEADER = 60
WINDOW_SIZE = TILE_SIZE *4

def pos_topleft(i):
    row = i // 4
    column = i % 4
    x_topleft = TILE_SIZE*column+GAP//2
    y_topleft = TILE_SIZE*row+GAP//2+HEADER

    return x_topleft, y_topleft


def reset_game():
    board = Board()
    board.shuffle()
    moves = 0
    time_start = pygame.time.get_ticks()
    time_clear = None
    history_blank = []
    played_clear_sound = False
    pos_draw = {}

    for i in range(16):
        number = board.tiles[i]
        pos_draw[number] = list(pos_topleft(i))


    return board, moves, time_start, time_clear, history_blank, pos_draw, played_clear_sound


def main():
    pygame.init()

    sound_slide = pygame.mixer.Sound(ASSETS/"slide.wav")
    sound_undo = pygame.mixer.Sound(ASSETS/"undo.wav")
    sound_clear = pygame.mixer.Sound(ASSETS/"clear.wav")

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE+HEADER))
    
    overlay_clear = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
    overlay_clear.fill((0,0,0))
    overlay_clear.set_alpha(150)

    pygame.display.set_caption("fifteen-puzzle")
    font = pygame.font.SysFont(None, 50)
    font_sub = pygame.font.SysFont(None, 36)

    clock = pygame.time.Clock()

    board, moves, time_start, time_clear, history_blank, pos_draw ,played_clear_sound= reset_game()
    
    while True:
        screen.fill((0,0,0))
        tiles_stopped = True

        for i in range(16):
            number = board.tiles[i]
            if number != 0:
                text = font.render(str(number), True, (0, 0, 0))

                x_goal, y_goal = pos_topleft(i)
                x_draw, y_draw = pos_draw[number]

                x_draw = x_draw + (x_goal -x_draw) * 0.2
                y_draw = y_draw + (y_goal -y_draw) * 0.2

                if abs(x_goal - x_draw) < 1 : x_draw = x_goal
                if abs(y_goal - y_draw) < 1 : y_draw = y_goal
                if x_draw != x_goal or y_draw != y_goal:
                    tiles_stopped = False

                pos_draw[number] = [x_draw, y_draw]

                rect = pygame.Rect(x_draw,y_draw, TILE_SIZE-GAP, TILE_SIZE-GAP)
                pygame.draw.rect(screen, (255,255,255), rect)

                text_rect = text.get_rect(center = rect.center)
                screen.blit(text, text_rect)

        text_moves = font.render(f"moves:{moves}", True, (255, 255, 255))
        text_rect = text_moves.get_rect(midleft = (10, HEADER // 2))
        screen.blit(text_moves, text_rect)


        time_passed = (pygame.time.get_ticks()-time_start)//1000        
        
        if board.is_solved():
            if time_clear is None:
                time_clear = time_passed
            if tiles_stopped:

                screen.blit(overlay_clear,(0, HEADER))

                text_clear = font.render("CLEAR!", True, (255, 0, 0))
                text_clear_rect = text_clear.get_rect(center = (WINDOW_SIZE//2,HEADER+WINDOW_SIZE//2))
                screen.blit(text_clear, text_clear_rect)

                text_result = font_sub.render(f"moves:{moves}, time:{time_clear}", True, (255, 255, 255))
                text_result_rect = text_result.get_rect(midtop = (text_clear_rect.centerx, text_clear_rect.bottom + 10))
                screen.blit(text_result, text_result_rect)

                if not played_clear_sound :            
                    sound_clear.play()
                    played_clear_sound = True

        if time_clear is None:
            text_time = font.render(f"time:{time_passed}", True, (255, 255, 255))
        else :
            text_time = font.render(f"time:{time_clear}", True, (255, 255, 255))

        text_rect = text_time.get_rect(midright = (WINDOW_SIZE - 10, HEADER//2))
        screen.blit(text_time, text_rect)
    
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if time_clear is None:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if event.pos[1] >= HEADER:
                            row_select = (event.pos[1]-HEADER) // TILE_SIZE
                            column_select = event.pos[0] // TILE_SIZE
                            index_select = 4 * row_select + column_select
                            former_blank = board.find_blank()
                            if board.move(index_select):
                                sound_slide.play()
                                history_blank.append(former_blank)
                                moves += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board, moves, time_start, time_clear, history_blank, pos_draw, played_clear_sound = reset_game()
                
                if time_clear is None:
                    if event.key == pygame.K_z:
                        if history_blank:
                            sound_undo.play()
                            board.move(history_blank.pop())
                            moves -= 1
        clock.tick(60)


if __name__ == "__main__":
    main()