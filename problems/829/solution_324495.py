def soma_h(N):
    """Retorna a média harmonica dos n termos;
    int -> float"""
    x = 1
    H = 0
    while x <= N:
        H += 1/x
        x += 1
    return round (H,2)