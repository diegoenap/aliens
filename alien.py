import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien on the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_ttings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien rigth."""
        self.x += (self.ai_ttings.alien_speed_factor * self.ai_ttings.fleet_direction)
        self.rect.x = self.x