def conta_numero(numero, matriz):
    ''''''
    resultado = 0
    indice = 0
    linhas = len(matriz)
    for i in range(linhas):
        if numero in matriz[i][:]:
            resultado += matriz[i].count(numero) 
        elif linhas == 0:
            return 0
        else:
            pass
    return resultado