import numpy as np
import random
import time

sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)

def enhanced_wind_mouse(start_x, start_y, dest_x, dest_y, G_0=9, W_0=3, M_0=15, D_0=12, 
                        obstacles=None, move_mouse=lambda x,y: None, pause_chance=0.1, jitter_chance=0.05):
    current_x, current_y = start_x, start_y
    v_x = v_y = W_x = W_y = 0
    adaptive_speed = M_0
    
    while (dist := np.hypot(dest_x-start_x, dest_y-start_y)) >= 1:
        W_mag = min(W_0, dist)
        
        if dist >= D_0:
            W_x = W_x/sqrt3 + (2*np.random.random() - 1) * W_mag/sqrt5
            W_y = W_y/sqrt3 + (2*np.random.random() - 1) * W_mag/sqrt5
        else:
            W_x /= sqrt3
            W_y /= sqrt3
            if M_0 < 3:
                M_0 = np.random.random() * 3 + 3
            else:
                M_0 /= sqrt5
        
        v_x += W_x + G_0 * (dest_x - start_x) / dist
        v_y += W_y + G_0 * (dest_y - start_y) / dist
        v_mag = np.hypot(v_x, v_y)
        
        adaptive_speed = max(3, M_0 * (dist / D_0))
        if v_mag > adaptive_speed:
            v_clip = adaptive_speed / 2 + np.random.random() * adaptive_speed / 2
            v_x = (v_x / v_mag) * v_clip
            v_y = (v_y / v_mag) * v_clip
        
        start_x += v_x
        start_y += v_y
        move_x = int(np.round(start_x))
        move_y = int(np.round(start_y))
        
        if current_x != move_x or current_y != move_y:
            if obstacles and (move_x, move_y) in obstacles:
                continue  # Skip this move to avoid obstacle
            
            if random.random() < pause_chance:
                time.sleep(random.uniform(0.1, 0.5))  # Simulate user pause
            
            if random.random() < jitter_chance:
                jitter_x = random.randint(-2, 2)
                jitter_y = random.randint(-2, 2)
                move_x += jitter_x
                move_y += jitter_y
            
            move_mouse(current_x := move_x, current_y := move_y)

    return current_x, current_y

# Example usage:
# Define the move_mouse function to print coordinates
def move_mouse(x, y):
    print(f"Mouse moved to: ({x}, {y})")

# Define obstacles as a set of coordinates
obstacles = {(50, 50), (51, 51), (52, 52)}

# Run the enhanced algorithm
start_x, start_y = 10, 10
dest_x, dest_y = 100, 100
enhanced_wind_mouse(start_x, start_y, dest_x, dest_y, obstacles=obstacles, move_mouse=move_mouse)



import matplotlib.pyplot as plt

fig = plt.figure(figsize=[13,13])
plt.axis('off')
for y in np.linspace(-200,200,25):
    points = []
    enhanced_wind_mouse(0,y,500,y,move_mouse=lambda x,y: points.append([x,y]))
    points = np.asarray(points)
    plt.plot(*points.T)
plt.xlim(-50,550)
plt.ylim(-250,250)

