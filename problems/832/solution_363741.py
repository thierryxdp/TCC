def eh_quadrada(numero):
    '''Função para identificar se a matriz é quadrada, list -> bool'''
    x = 0
    y = 0
    for i in range(len(numero)):
        if x != 0:
            x = x + 1
            for j in range(len(numero[0])):
                if x == 0:
                    return True
                elif x == y:
                    return True
        else:
            return False