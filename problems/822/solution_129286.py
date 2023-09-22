def repetidos(lista):
    """Essa função recebe uma lista de numeros e conta quantas vezes numeros consecutivos se repetem
    list ->int"""
    contador = 0
    for x in range(len(lista)-1):
        if lista[x] == lista[x+1]:
            contador += 1
    return contador