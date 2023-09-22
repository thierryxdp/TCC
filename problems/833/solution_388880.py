def conta_numero(numero, matriz):
    '''Função retorna a quantidade que um número repete em uma matriz
       int, list-->int '''
    i=0
    j=0
    resultado=0
    while i<len(matriz):
        while j<len(matriz[0]):
            if numero==matriz[i][j]:
                resultado+=1
            j=j+1
        i=i+1
        j=0
    return resultado