def media_matriz(matriz):
    '''função que dada uma matriz retorna a média de todos os 
    números dessa matriz com duas casas decimais'''
    total = 0
    soma = 0
    for i in range(len(matriz)):
        contador = 0
        while contador < len(matriz[0]):
            soma = soma + matriz[i][contador]
            total = total + 1
            contador = contador + 1
    media = soma/total
    return media