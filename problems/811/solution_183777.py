def colchao(medidas, H, L):
    """Recebe as medidas de um colcaho e de uma porta e retora se o colchao passa pela porta"""
    porta = [H, L].sort()
    return porta
    return all(p > c for (p, c) in zip(porta, colchao))