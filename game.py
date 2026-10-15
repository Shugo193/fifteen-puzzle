import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("fifteen-puzzle")

    clock = pygame.time.Clock()

    while True:
        screen.fill((0,0,0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)

        
if __name__ == "__main__":
    main()