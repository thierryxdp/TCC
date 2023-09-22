def colchao(medidas,h,l):
    if medidas[2]>h and medidas[1]>l:
        return bool(0)
    if medidas[0]>l:
        return bool(0)
    if medidas[2]<h and medidas[0]<l:
        return bool(1)
    if medidas[2]>h and medidas[1]<h:
        return bool(1)
    else:
        return bool(1)