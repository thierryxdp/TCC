def eh_quadrada(numero):
    '''Função para identificar se a matriz é quadrada, list -> bool'''
    for i in range(len(numero)):
        if i != 0:
            i = i + 1
            for j in range(len(numero[0])):
                if i == 0:
                    return True
                if i == j:
                    return True
                else:
                    return False
        else:
            return False