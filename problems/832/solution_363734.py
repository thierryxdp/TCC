def eh_quadrada(numero):
    '''Função para identificar se a matriz é quadrada, list -> bool'''
    x = 0
    y = 0
    for i in range(len(numero)):
        x = x + 1
        for j in range(len(numero[0])):
            y = y + 1
    if i == 0:
        return False
    elif i == j:
        return False
    else:
        return True