def media_matriz(matriz):
    '''função que retorna a media de uma matriz:list->float'''
    matriz = []
    qtd = 0
    elemento = len(matriz)
    for linha in matriz:
        for elemento in matriz: 
            qtd+=1
    qtd = qtd//elemento
    return round(qtd)