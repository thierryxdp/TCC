def conta_numero(matriz, numero):
    '''funcao que retorna a quantidade de numeros na matriz
list, float-> int'''
    assert(len(matriz)>0) and (len(matriz[0])>0)
    ocorrencias = 0
    for linha in matriz:
        for elemento in linha:
            if (elemento == numero):
                ocorrencias = ocorrencias + 1
    return ocorrencias