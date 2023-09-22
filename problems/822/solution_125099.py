def repetidos(numeros):
    """Recebe uma lista de numeros e retorna o número de vezes
    que um elemento é igual ao elemento anterior;
    list -> int"""
    qtd_iguais = 0
    i = 0
    while i < len(numeros):
        if numeros[i] == numeros[i-1]:
            qtd_iguais += 1
        i += 1
    return qtd_iguais