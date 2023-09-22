def colchao(medidas,h,l):
    medidas = [a,b,c]
    acolchao = 2*a*b + 2*a*c + 2*b*c
    aporta = h*l
    if acolchao > aporta:
        return false
    else:
        return true