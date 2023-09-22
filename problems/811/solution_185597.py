def colchao(medidas: list[int], h : int, l : int) -> bool:
    """ """
    if (medidas[1] => h) or( h => medidas[1]):
        return True
    else:
        return False