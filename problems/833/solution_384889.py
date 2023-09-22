def conta_numero(numero, matriz):
    """Funçáo que dado um numero busca o mesmo na matriz dada
    int, int -> int"""
    contador = 0

    for i in range (len(matriz)):
        if numero in matriz[i]:
            
            return list.count(numero(matriz))