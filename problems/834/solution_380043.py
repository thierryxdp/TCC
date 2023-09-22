def media_matriz(matriz):
    '''funcao que recebe uma matriz e retorna a media da soma 
       de todos os numeros dela.
       list(list) -> float'''
    i= 0
    soma= 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            soma += matriz[x][y]
            i += 1
    return round((soma/i),2)