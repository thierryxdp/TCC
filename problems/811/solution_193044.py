def colchao(medidas,H,L):
    'funcao que resolva se o colchao passa pela porta ou nao'
    x = medidas
    z = H+L
    if x < z:
        return True
    else:
        if x >= z:
            return False