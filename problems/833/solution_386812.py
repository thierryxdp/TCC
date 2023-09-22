def conta_numero(numero, matriz):
    """Função qe dado um valor int e uma matriz conta e retorna quantas vezes 
    o número aparece"""
    contador = 0
    for i in range(len(matriz)):
        for n in range(len(matriz[i])):
            if numero == matriz[i][n]:
            	contador+=1
    return contador