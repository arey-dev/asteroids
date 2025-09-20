import sys

import pygame

from player import *
from asteroid import *
from constants import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)

    Asteroid.containers = (asteroids, updatables, drawables)

    AsteroidField.containers = (updatables)

    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        
        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)

        for asteroid in asteroids:
            if player.did_collide(asteroid):
                print("Game over!")
                sys.exit(0)

            for shot in shots:
                if shot.did_collide(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()


