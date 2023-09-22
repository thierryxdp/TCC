def colchao(medidas,h,l):
    acolchao = 2*medidas[2]*medidas[1] + 2*medidas[1]*medidas[2] + 2*medidas[2]*medidas[0]
    aporta = h*l
    if acolchao >= aporta:
        return False
    else:
        return True