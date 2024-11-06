
import pygame
import math

from constants import *


class Star:

    def __init__(self, x, y, mass):
        self.x = x  # X position of the star
        self.y = y  # Y position of the star
        self.mass = mass  # Mass of the star (affects gravitational pull and size)
        self.radius = math.sqrt(mass)  # Radius of the star (for drawing purposes)
        
        # Initialize velocity and acceleration as vectors
        self.velocity_x = 0  # X component of velocity
        self.velocity_y = 0  # Y component of velocity
        self.acceleration_x = 0  # X component of acceleration
        self.acceleration_y = 0  # Y component of acceleration

    def check_collision(self, other, distance):
        """
        Checks if the star is colliding with the other star.
        Returns True if the stars are colliding, False otherwise.
        """
        return distance < self.radius+other.radius


    def apply_gravitational_force(self, other):
        """
        Calculates and applies the gravitational force exerted by another star.
        Uses Newton's law of gravitation: F = G * (m1 * m2) / r^2
        Updates the star's acceleration based on this force.
        """

        # Calculate distance components and magnitude
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2) 

        if self.check_collision(other, distance):
            return "collide"

        # Calculate force magnitude
        force = G * (self.mass * other.mass) / (distance**2)

        # Calculate direction of force (normalized vector)
        force_x = force * dx / distance
        force_y = force * dy / distance

        # Apply force to acceleration (F = ma => a = F / m)
        self.acceleration_x += force_x / self.mass
        self.acceleration_y += force_y / self.mass
        
        return None


    def update_position(self):
        """
        Updates the star's position based on its velocity and acceleration.
        Resets acceleration after each update.
        """
        # Update velocity with current acceleration
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y

        # Update position with current velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Reset acceleration for next iteration
        self.acceleration_x = 0
        self.acceleration_y = 0


    def draw(self, screen):
        """
        Draws the star on the given Pygame screen surface.
        """
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), int(self.radius))
    
    
    def is_offscreen(self):
        """
        Checks if the star is off-screen and should be removed.
        """
        return not (-OFF_SCREEN_BUFFER < self.x < WIDTH + OFF_SCREEN_BUFFER and -OFF_SCREEN_BUFFER < self.y < HEIGHT + OFF_SCREEN_BUFFER)
        
    
    @staticmethod
    def merge_stars(star1, star2):
        """
        Merges two stars into a single star with combined mass and momentum.
        Returns the new merged star.
        """
        # Combine masses and calculate the new position and velocity by momentum conservation
        combined_mass = star1.mass + star2.mass
        new_x = (star1.x * star1.mass + star2.x * star2.mass) / combined_mass
        new_y = (star1.y * star1.mass + star2.y * star2.mass) / combined_mass

        # Calculate combined velocities
        new_velocity_x = (star1.velocity_x * star1.mass + star2.velocity_x * star2.mass) / combined_mass
        new_velocity_y = (star1.velocity_y * star1.mass + star2.velocity_y * star2.mass) / combined_mass

        # Create a new merged star
        new_star = Star(new_x, new_y, combined_mass)
        new_star.velocity_x = new_velocity_x
        new_star.velocity_y = new_velocity_y
        return new_star
