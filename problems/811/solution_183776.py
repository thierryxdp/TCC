def colchao(medidas, H, L):
    porta = [H, L].sort()
    return all(p > c for (p, c) in zip(porta, colchao))