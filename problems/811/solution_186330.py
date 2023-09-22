def colchao(medidas,h,l):
    if medidas[2]>h:
        return bool(0)
    if medidas[0]>medidas[1]:
        return bool(0)
    else:
        return bool(1)