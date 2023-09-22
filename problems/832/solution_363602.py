def eh_quadrada(matriz):
    '''Recebe uma matriz e identifica se a matriz é quadrada ou não.
    list -> bool'''
    soma = []
    
    for i in matriz:
        soma += [i]
    if sum(soma) % 2 == 0:
        return True
    else:
        return False