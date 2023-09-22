def colchao(medidas: list[int], h : int, l : int) -> bool:
    if medidas[0] <= h and medidas[1] >= l:
        return True
    else:
        return False