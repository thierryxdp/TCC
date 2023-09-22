def colchao(medidas,h,l):
    acolchao = 2*medidas[0]*medidas[1] + 2*medidas[0]*medidas[2] + 2*medidas[1]*medidas[2]
    aporta = h*l
    if aporta >= acolchao:
        return True
    else:
        return False