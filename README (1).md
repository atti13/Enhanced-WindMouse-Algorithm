
# Enhanced WindMouse Algorithm

## Overview

The Enhanced WindMouse algorithm simulates human-like mouse movements by incorporating several enhancements to the original WindMouse algorithm. These improvements make the movements more natural and harder to detect as automated actions.

## Features

1. **Adaptive Speed Control**: Adjusts the speed of the mouse movement dynamically based on the distance to the destination.
2. **Obstacle Avoidance**: Ensures the mouse avoids predefined obstacles or specific regions on the screen.
3. **User Behavior Simulation**: Adds realistic user behavior patterns such as pauses and small jitters.

## Algorithm Explanation

### Initialization

- **Current Position**: The starting coordinates of the mouse.
- **Velocity Components**: `v_x` and `v_y` initialized to zero.
- **Wind Components**: `W_x` and `W_y` initialized to zero.

### Main Loop

The main loop continues until the distance to the destination is less than 1 pixel.

1. **Distance Calculation**:
   - The distance to the destination is calculated using the Euclidean distance formula.

2. **Wind Magnitude**:
   - The wind magnitude (`W_mag`) is limited to the minimum of a predefined value (`W_0`) or the current distance.

3. **Wind Components Update**:
   - When far from the destination, wind components are updated with random fluctuations.
   - When close to the destination, wind components are damped to help the mouse settle at the destination.

4. **Velocity Update**:
   - The velocity components are updated by combining wind and gravitational forces.
   - The gravitational force pulls the mouse towards the destination.
   
5. **Adaptive Speed Control**:
   - The speed (`adaptive_speed`) is dynamically adjusted based on the distance to the destination, ensuring natural speed variation.

6. Velocity Clipping:
   - If the velocity magnitude exceeds the adaptive speed, it is clipped to simulate more realistic movements.

7. Position Update:
   - The current position is updated by adding the velocity components.
   - The new position is rounded to integer values for pixel coordinates.

### Additional Enhancements

1. Obstacle Avoidance:
   - Before moving the mouse to a new position, it checks if the new position intersects with any predefined obstacles.
   - If an obstacle is detected, the move is skipped to simulate avoidance behavior.

2. User Behavior Simulation:
   - Random Pauses: Introduces random pauses with a certain probability to simulate natural user behavior.
   - Jitters: Adds small random jitters to the position to mimic human hand movements.

## Usage

The enhanced WindMouse algorithm can be used in various applications where human-like mouse movements are needed, such as automated testing, bot creation, and user interface interactions.


## Conclusion

The Enhanced WindMouse algorithm provides a robust and realistic simulation of human-like mouse movements, making it suitable for applications requiring undetectable automated actions.
