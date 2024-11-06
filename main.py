import pygame
import sys

from star import Star
from constants import *

# Initialize Pygame
pygame.init()

FONT = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gluttony Star Gravity Simulation")

# Create a list to store all stars
stars = []

# Text input mode variables
input_mode = False
input_text = ""
input_position = (0, 0)

# Main simulation loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN and not input_mode:
            if event.button == 1:  # Left mouse button
                # Enable input mode and set the input position
                input_mode = True
                input_position = event.pos
                input_text = ""  # Clear previous input text
            
            if event.button == 3: # Right mouse button
                # Delete the star you click on
                for star in stars:
                    distance = ((star.x - event.pos[0])**2 + (star.y - event.pos[1])**2)**0.5
                    if distance < star.radius:
                        stars.remove(star)
                    
        #keyboard input for mass entry
        elif event.type == pygame.KEYDOWN and input_mode:
            if event.key == pygame.K_RETURN:  # Enter key confirms input
                try:
                    mass = float(input_text)
                    if mass >= 1:
                        # Create a new star with the mass u want
                        new_star = Star(input_position[0], input_position[1], mass)
                        stars.append(new_star)
                    elif mass < 1:
                        print("Come on, have you ever seen a star with negative mass ?")
                    else:
                        mass = 1
                except ValueError:
                    print("Please enter a valid number for the mass.")
                
                # Exit input mode
                input_mode = False
                input_text = ""
            elif event.key == pygame.K_ESCAPE:  # Escape key cancels input
                input_mode = False
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                input_text = input_text[:-1]
            else:
                # Append typed character to input text
                input_text += event.unicode

    if not input_mode:
        # Update each star's gravitational interaction
        collided_stars = []
        new_stars = []
        for star in stars:
            for other_star in stars:
                if star != other_star:  # Avoid self-interaction
                    if star.apply_gravitational_force(other_star) == "collide" and star not in collided_stars and other_star not in collided_stars:
                        collided_stars += [star, other_star]
                        new_stars.append(Star.merge_stars(star, other_star))
        
            # Update position after applying forces
            star.update_position()
            if star.is_offscreen():
                stars.remove(star)

        # Remove collided stars and add the new bigger stars
        for star in collided_stars:
            if star in stars: stars.remove(star)
        for star in new_stars:
            if star not in stars: stars.append(star)

    # Display
    screen.fill(BLACK)  # Clear the screen with black background
    for star in stars:
        star.draw(screen)

    # Render input text if in input mode
    if input_mode:
        # Render the input text
        text_surface = FONT.render(f"Enter mass: {input_text}", True, WHITE)
        screen.blit(text_surface, (input_position[0], input_position[1] - 30))

    pygame.display.flip()  # Update the display

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
