def faltante(lista):
    """funcao que retorna o numero que falta em um intervalo numero de uma lista;
    list -> int"""

    lista.sort()
    i = 0
    f = int()
    n = []
    

    while i<len(lista):
        if lista[i] not in list(range(lista[0],lista[len(lista)-1])):
            n.append(lista[i])

        i = i+1

    return n