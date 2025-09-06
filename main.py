from utils.rng import RNG
from generators import noise
from postprocess import biome_assign
from render import pygame_renderer

def main():
    rng = RNG(seed=42)
    grid = noise.generate_noise_map(20, 40, rng)
    biomes = biome_assign.assign_biomes(grid)
    pygame_renderer.render(biomes, cell_size=20)

if __name__ == "__main__":
    main()
