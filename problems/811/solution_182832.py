def colchao(medidas,H,L):
    '''função recebe como entrada as medidas de uma colchão e de uma porta, e retorna True caso seja possível passar o colchão por essa porta
    list, int, int -> bool'''
    a, b, c = medidas
    if a*b > H*L or a*c > H*L
        return False
    else:
        return True