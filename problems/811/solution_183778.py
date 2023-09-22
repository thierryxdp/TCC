def colchao(medidas, H, L):
    """Recebe as medidas de um colcaho e de uma porta e retora se o colchao passa pela porta"""
    porta = [H, L]
    porta.sort()
    return all(p > c for (p, c) in zip(porta, colchao))