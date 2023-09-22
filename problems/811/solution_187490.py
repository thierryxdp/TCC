def colchao(medidas,H,L):
    medidaB=medidas[1]
    medidaC=medidas[2]
    if medidaC>L:
        if medidaB>H:
            return False
        else:
            return True
    if medidaC<L:
        return True