def conta_numero (numero, matriz):
    """Recebe um número e uma matriz e retorna o número de 
    vezes que o número se repete na matriz.
    int, list -> int"""
    total = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                total += 1
    return total