def colchao(medidas,H,L):
    '''função recebe como entrada as medidas de uma colchão e de uma porta, e retorna True caso seja possível passar o colchão por essa porta
    list, int, int -> bool'''
    a, b, c = medidas
    if b > H and c > H or b > L and c > L:
        return False
    else:
        return True