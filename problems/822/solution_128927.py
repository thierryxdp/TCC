def repetidos(lista):
    """Essa função recebe uma lista de numeros e conta
    quantas vezes numeros consecutivos se repetem
    list ->int"""
    contador = 0
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            contador += 1
    return contador