import math

# -----------------------------
# Helper: Euclidean distance
# -----------------------------
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# -----------------------------
# Helper: compute mean of points
# -----------------------------
def mean(points):
    if len(points) == 0:
        return (0, 0)
    x = sum([p[0] for p in points]) / len(points)# sum of x-coordinates 
    y = sum([p[1] for p in points]) / len(points)# sum of y-coordinates 
    return (x, y)

# -----------------------------
# K-means implementation
# -----------------------------
def kmeans(points, k=2, iterations=10):
    # Step 1: initialize centroids (pick first k points)
    centroids = points[:k]
    print("Initial centroids:", centroids)

    for xx in range(iterations):
        # Step 2: assign points to nearest centroid
        clusters = [[] for _ in range(k)]
        for p in points:
            distances = [distance(p, c) for c in centroids]
            #print("Distances from point", p, "to centroids:", distances)
            closest = distances.index(min(distances))
            clusters[closest].append(p)
            

        # Step 3: update centroids
        new_centroids = [mean(cluster) for cluster in clusters]

        # Stop if centroids do not change
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return clusters, centroids


# -----------------------------
# Example data
# -----------------------------
points = [
    (1, 1),
    (1.5, 2),
    (3, 4),
    (3.5, 5),
    (4.5, 5),
    (5, 7)
]

clusters, centroids = kmeans(points, k=2)

print("Clusters:", clusters)
print("Centroids:", centroids)


