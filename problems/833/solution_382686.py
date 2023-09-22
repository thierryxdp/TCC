def conta_numero(numero, matriz):
    ''''''
    resultado = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        if [] in matriz[i][:]:
            return 0
        if numero in matriz[i][:]:
            resultado += matriz[i].count(numero) 
        else:
            pass
    return resultado