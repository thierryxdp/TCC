def colchao(medidas,H,L):
    '''função recebe como entrada as medidas de uma colchão e de uma porta, e retorna True caso seja possível passar o colchão por essa porta
    list, int, int -> bool'''
    a, b, c = medidas
    if a > H and b > H and c > H or a > L or b > L or c > L:
        return False
    else:
        return True