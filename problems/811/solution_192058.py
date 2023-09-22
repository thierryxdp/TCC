def colchao(medidas,H,L):
    '''Função para saber de consegue passar o colchão pela porta
    list,int -> bool'''

    [A,B,C] = medidas 

    if medidas[1] <= H:
        return True
    elif medidas[1] <= L:
        return True    
    else:
        return False