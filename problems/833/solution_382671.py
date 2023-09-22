def conta_numero(numero, matriz):
    ''''''
    resultado = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        if numero in matriz[i][:]:
            resultado += matriz[i].count(numero) 
        else:
            return 0
    return resultado