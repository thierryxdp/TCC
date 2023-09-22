def colchao(medidas, h, l):
    medidas = []
    if medidas > (h and l):
        return True
    if medidas < h and l:
        return False