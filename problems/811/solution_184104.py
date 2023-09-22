def colchao(medidas,H,L):
    '''Função que dadas as medidas de um colchão em ordem crescente
    contidas em uma lista e as medidas da porta, ambas em centímetros 
    retorna True para o caso do colchão passar pela porta e False para
    o caso de não passar. list, int, int -> bool'''
    if medidas[0,1] > H:
        return False
    else:
        return True