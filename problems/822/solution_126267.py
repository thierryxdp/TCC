def repetidos(numeros):
    """Recebe uma lista de números e retorna a quantidade de vezes
    que um elemento é igual ao seu antecessor.
    lista -> int"""
    
    i = 0
    quant = 0
    while i < len(numeros):
        if i > 0 and numeros[i] == numeros[i-1]:
            quant += 1
        i += 1
    return quant