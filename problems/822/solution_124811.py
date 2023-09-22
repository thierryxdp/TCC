def repetidos(lista):
    """Retorna a quantidade de repetições seguidas que ocorrem em uma determinada lista. list -> int"""
    repetidor = 0
    contador = 0
    while repetidor < len(lista):
        if lista[repetidor] == lista[repetidor -1]:
            contador = contador + 1
        repetidor = repetidor + 1
    return contador