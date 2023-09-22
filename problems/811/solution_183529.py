def colchao(medidas, H,L):
    """Retorna se o colchao passa ou nao pela porta
       Entrada: list, int, int
       Saída: bool
     """
    if medidas[1]>H:
        return False
    if medidas[1]<=H:
        return True