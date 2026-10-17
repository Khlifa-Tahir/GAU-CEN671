import random

# Objective function
def f(x):
    return x * x  # minimize this

# Search space
search_space = [-5, -3, -1, 0, 1, 3, 5]

# Initialize employed bees (each bee has a position)
bees = [-5, -1, 3]  # starting points
best = bees[0]
best_value = f(best)

for iteration in range(5):  # few simple rounds
    print("\nIteration", iteration + 1)

    # Employed bees phase: try small changes
    for i in range(len(bees)):
        current = bees[i]
        # pick a nearby value randomly
        neighbor = random.choice(search_space)
        if f(neighbor) < f(current):
            bees[i] = neighbor  # move to better flower

    # Onlooker bees phase: choose best solutions
    # (simplified: pick the best among current bees)
    best_bee = min(bees, key=f)
    if f(best_bee) < best_value:
        best = best_bee
        best_value = f(best_bee)

    # Scout bee phase: replace worst bee with random new one
    worst_bee = max(bees, key=f)
    bees[bees.index(worst_bee)] = random.choice(search_space)

    print("Bees:", bees)
    print("Best so far:", best, "with f(x) =", best_value)

print("\nFinal best solution:", best, "with f(x) =", best_value)
