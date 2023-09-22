def colchao(medidas,h,l):
    acolchao = medidas[2]*medidas[0]
    aporta = h*l
    if acolchao <= aporta:
        return True
    else:
        return False