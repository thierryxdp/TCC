def media_matriz(matriz_inteiros2):
    quant_colunas = len(matriz_inteiros2[0])
    quant_linhas = len (matriz_inteiros2)
    soma_elementos = 0
    for listas in matriz_inteiros2:
        for i in range(len(listas)):
            soma_elementos += sum(listas)
            quant_elementos = quant_colunas + quant_linhas
        mediaMatriz = (soma_elementos)/quant_elementos
    return round (mediaMatriz,2)