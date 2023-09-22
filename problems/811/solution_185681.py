def colchao(medidas: list[int], h : int, l : int) -> bool:
    if medidas[1] < h and medidas[2] > l:
        return True
    elif medidas[1]>h and medidas[2]<1:
        return true
    else:
        return false