def conta_numero(numero, matriz):
    quantidadenumeros=0
    for lin in range(len(matriz)):
        quantidade=list.count(matriz[lin], numero)
        quantidademumero = quantidadenumero + quantidade
        return