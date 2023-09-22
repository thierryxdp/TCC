def colchao(medidas: list[int], h : int, l : int) -> bool:
    """ """
    if (medidas[1] >= h or medidas[1] <= h) and medidas[2] >= l:
        return True
    else:
        return False