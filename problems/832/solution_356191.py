def eh_quadrada(matriz):
    '''Função identifica se uma dada matriz é quadrada ou não;
    list -> bool'''
    l_matriz= len(matriz)
    c_matriz = len(matriz[0])

    if l_matriz == c_matriz or matriz == []:
        return True
    else:
        return False

# O teste 21 apresenta a entrada INCORRETA!!!!!!!!!!!!!!!!!