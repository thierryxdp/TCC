def repetidos(lista):
    """Função que recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior,
    lista --> int"""
    cont = 0
    i = 0
    while i < len(lista):
        if i == 0:
            i += 1
            continue
        else:
            if lista[i] == lista[i-1]:
                cont += 1
        i += 1
    return cont