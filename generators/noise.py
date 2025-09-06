def generate_noise_map(rows, cols, rng):
    """Gera um mapa simples de ruído (mock)"""
    return [[rng.randint(0, 2) for _ in range(cols)] for _ in range(rows)]
