import numpy as np
import matplotlib.pyplot as plt
import math


# -----------------------------
# Minimum Enclosing Circle (simple version)
# -----------------------------
def min_enclosing_circle(points):
    points = np.array(points)
    
    # Compute all pairwise distances
    max_d = 0
    p1, p2 = None, None
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = np.linalg.norm(points[i] - points[j])
            if d > max_d:
                max_d = d
                p1, p2 = points[i], points[j]
    
    # Center = midpoint of farthest pair
    center = (p1 + p2) / 2
    radius = max_d / 2+0.5
    
    return center, radius

# -----------------------------
# Your points
# -----------------------------
points       = [(-4, -3), (-1, 2), (4, 3), (5,6)]
search_space = [(-5, -3), (-1, 0), (1, 3), (5,6)]

nearest = min(points, key=lambda s: math.dist(s ,(5,4)))

print("Nearest point in search space to (2,1):", nearest)



center, radius = min_enclosing_circle(points)
print("Center:", center)
print("Radius:", radius)

# -----------------------------
# Plot
# -----------------------------
fig, ax = plt.subplots(figsize=(4, 4))

# Plot points
px, py = zip(*points)
ax.scatter(px, py, color='blue', s=20, label='Points')

# Plot circle
circle = plt.Circle(center, radius, color='red', fill=False, linewidth=1.5)
ax.add_patch(circle)

# Plot center
ax.scatter(0, 0, color='black', s=20, marker='x', label='Origin')
ax.scatter(center[0], center[1], color='red', s=20, marker='x', label='Center')
ax.scatter(nearest[0], nearest[1], color='green', s=20, marker='o', label='Nearest Point')
# Formatting
ax.set_aspect('equal', 'box')
ax.grid(True)
#ax.legend()
ax.set_title("Minimum Enclosing Circle")

plt.show()
