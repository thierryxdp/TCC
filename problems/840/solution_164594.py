def bolos(A,B,C):
    '''Calcula a maior quantidade inteira de bolo possivel de se fazer dados 
    ingredientes A=farinha,B=ovos e C=leite'''
    return max((A//2),(B//3),(C//5))