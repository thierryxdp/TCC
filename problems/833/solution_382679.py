def conta_numero(numero, matriz):
    ''''''
    resultado = 0
    indice = 0
    while indice < len(matriz[0]):
        linhas = len(matriz)
        colunas = len(matriz[0])
        for i in range(linhas):
            if numero in matriz[i][:]:
                resultado += matriz[i].count(numero) 
            else:
                pass
            indice += 1
            
    return resultado