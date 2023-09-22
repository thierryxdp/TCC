def conta_numero(numero,matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    contador = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if numero == matriz[i][j]:
                contador+=1
    return contador