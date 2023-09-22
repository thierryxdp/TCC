def media_matriz(matriz):
    '''Função que dado uma matriz,retorna a media de todos os numeros.
    list->float'''
    soma=0
    for linha in matriz:
           for elemento in linha:
               soma=soma+elemento
               x=soma/(len(matriz)*len(matriz[0]))
    return round(x,2)