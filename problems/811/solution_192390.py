def colchao(medidas,h,l):
    acolchao = medidas[0]*medidas[1]
    aporta = h*l
    if acolchao >= aporta:
        return False
    else:
        return True