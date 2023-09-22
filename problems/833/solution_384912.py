def conta_numero(numero, matriz):
    """Função que dado um numero busca o mesmo na matriz dada
    int, int -> int"""
    contador=0

    for i in len(matriz):
        if numero in matriz[i]:
            contador+=1
    return contador