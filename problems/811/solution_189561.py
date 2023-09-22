def colchao(medidas,H,L):
    '''Dadas as medidas do colchão e a altura (h) e a largura (l) da porta, em centímetros, a função retorna True ou False para caso o colhão passe ou não pela porta; list,str,str -> bool'''
    soma1 = 0
    soma2 = 0
    
    if H>L or H==L:
        if medidas[0]>H:
            soma1 = soma1 + 1
        if medidas[1]>H:
            soma1 = soma1 + 1
        if medidas[2]>H:
            soma1 = soma1 + 1
    if H<L:
        if medidas[0]>L:
            soma2 = soma2 + 1
        if medidas[1]>L:
            soma2 = soma2 + 1
        if medidas[2]>L:
            soma2 = soma2 + 1

    if soma1 > 1 or soma2> 1:
        return False
    else:
        return True