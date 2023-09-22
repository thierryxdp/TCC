def media_matriz(matriz):
    
    elementos = []
    for i in range(len(matriz)):
        for n in matriz[i]:
            elementos = elementos + [n]
    linhas = len(matriz)
    colunas = len(matriz[0])
    return (sum(elementos))/(linhas*colunas)