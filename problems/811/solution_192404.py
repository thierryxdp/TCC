def colchao(medidas,h,l):
    acolchao =  2*medidas[1]*medidas[2] + 2*medidas[1]*medidas[0] + 2*medidas[2]*medidas[2]
    aporta = h*l
    if acolchao >= aporta:
        return False
    else:
        return True