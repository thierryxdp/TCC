def media_matriz(matriz):
    '''função que retorna a media de uma matriz:list->float'''
    matriz = []
    linha = len(matriz)
    elemento = len(matriz[0])
    coluna = elemento/linha
    qtd = 0
    for linha in matriz:
        for elemento in matriz: 
            qtd+=1
    qtd = qtd/elemento
    return round(qtd)