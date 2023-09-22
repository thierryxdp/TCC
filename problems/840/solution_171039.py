def bolos(far, ovo, leite):
    '''função que retorna a quantidade de bolos que pode ser feita com base na quantidade de ingredientes suficientes para medidas exatas. int, int, int --> int'''
    return math.floor(min((far/2), (ovo/3), (leite/5)))