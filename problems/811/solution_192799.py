def colchao(medidas,H,L):
    'função que recebe 3 entradas de colchão e porta e retorna True ou False com list-bool'
    if medidas[1]<=H or medidas[2]<=L:
        return True
    else:
        return False