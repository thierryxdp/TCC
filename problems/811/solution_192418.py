def colchao(medidas,h,l):
    acolchao = medidas[1]*medidas[2]
    aporta = h*l
    if aporta <= acolchao:
        return False
    else:
        return True