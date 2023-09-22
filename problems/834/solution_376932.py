def media_matriz(matriz): 
    contador=0
    qtd=0
    for linha in matriz:
        for elementos in linha:
            	contador=contador+elementos
                qtd=qtd+1
    return contador/