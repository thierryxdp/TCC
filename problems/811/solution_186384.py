def colchao(medidas, H, L):
    """Determina se o colchão de medidas (medidas) passa por uma porta de altura (H) e largura (L)
    list, int, int -> bool """
    dimensoes = [H, L]
    for i in range(2):
        if min(medidas)<min(dimensoes):
            medidas.remove(min(medidas))
            dimensoes.remove(min(dimensoes))
        else:
            return False
    return True