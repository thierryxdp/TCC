def media_matriz(matriz):
    '''função que recebe uma matriz como entrada e retorna a média de todos os números
       list -> int'''
    i=0
    soma=0
    for linha in matriz:
        for elemento in linha:
            soma= soma+ elemento
    return media