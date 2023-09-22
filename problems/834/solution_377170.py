def media_matriz(matriz:list) ->float:
    '''Recebe uma matriz e retorna a média dos valores de todos os elementos'''
    soma = 0
    for lista in matriz:
        for elemento in lista:
            soma += elemento
    media = soma/(len(matriz)*len(matriz[0])
   return media