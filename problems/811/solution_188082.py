def colchao(medidas, H, L):
    """Informa se um colchão com dadas 'medidas' passa por uma porta de altura H e largura L.
	Entrada: lista, float, float
    Saída: bool
    """
    if medidas[0] <= L and medidas[1] <= H:
        return True
    else:
        return False