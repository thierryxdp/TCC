def eh_quadrada(numero):
    '''Função para identificar se a matriz é quadrada, list -> bool'''
    x = 0
    y = 0
    for i in range(len(numero)):
        if i != 0:
            x = x + 1
            for j in range(len(numero[0])):
                if j == 0:
                    return True
                elif i == j:
                    return True
        else:
            return False