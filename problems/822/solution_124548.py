def repetidos(lista:list) -> int:
    """comentário"""
    i = 0
    numeros_rep = []
    while i < len(lista):
        if lista[i] == lista[i-1]:
            numeros_rep.append(lista[i])
        i += 1
    repetidos = len(numeros_rep)
    return repetidos