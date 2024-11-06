# Star Gravity Simulation

A simple gravity simulation using Pygame, where stars are created by the user and interact with each other through gravitational forces. Stars attract each other, merge on collision, and disappear when they drift too far from the screen.
Be aware that this model can be used like a N-Body simulation with a small amount of objects. It is NOT scalable for too high number of stars due to its complexity of o(n²).

## Features and usage

- **Create Stars**: Click on any location on the screen to create a star. Enter the star's mass in the input box that appears and press "Enter" to confirm or "Escape" to cancel.
- **Remove Stars**: Right click on a star to make it disapear.
- **Simulation Controls**:
    - Stars exert gravitational forces on each other, affecting each star's position and velocity based on Newton's law of gravitation.
    - When stars get too close, they merge into a larger star, preserving mass and momentum (gluttonous stars).
    - If a star moves too far off-screen, it will be removed from the simulation.

## Getting Started

### Prerequisites

- Python 3.x
- [Pygame](https://www.pygame.org/wiki/GettingStarted)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Adri-dou/Gluttony-Star-Gravity-Simulation
    cd Gluttony-Star-Gravity-Simulation
    ```

2. Install the required packages:
    ```bash
    pip install pygame
    ```

3. Run the simulation:
    ```bash
    python main.py
    ```

## Code Structure

- **`Star` Class**: Represents each star, with properties for position, mass, velocity, and gravitational force calculations.
- **Constants file**: Just stores the constants that are used in the otherr files XD.
- **Main Pygame Loop**: Handles user input, updates star positions, detects collisions, and manages rendering.

## Contributing

Feel free to submit issues or pull requests to suggest improvements or add features !

---

Have fun !
