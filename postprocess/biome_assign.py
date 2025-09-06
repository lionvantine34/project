def assign_biomes(grid):
    print("assign_biomes foi chamada!")
    mapping = {0: "water", 1: "grass", 2: "mountain"}
    return [[mapping.get(cell, "unknown") for cell in row] for row in grid]