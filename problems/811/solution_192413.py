def colchao(medidas,h,l):
    acolhao = medidas[2]*medidas[0]
    aporta = h*l
    if acolchao <= aporta:
        return True
    else:
        return False