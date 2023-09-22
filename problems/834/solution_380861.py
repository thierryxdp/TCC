def media_matriz(matriz):
    """
    	Recebe uma <matriz> e retorna a média de todos os 
        números da matriz.
        list --> float
    """
    todosNumerosDaMatriz = []
    for elementos in matriz:
       	for numero in elementos:
            todosNumerosDaMatriz += [numero]
            
    operacaoMedia = sum(todosNumerosDaMatriz)/len(todosNumerosDaMatriz)
    Media = round(operacaoMedia, 2)
    return Media