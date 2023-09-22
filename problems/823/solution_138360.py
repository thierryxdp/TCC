def faltante(lista):
    """Recebe uma lista de numeros e retorna qual numero esta
    faltando.
    list --> int"""
    i = 0
    list.sort(lista)
    if lista[0] > 1:
        return 1
    elif lista[len(lista) - 1] == len(lista):
        return len(lista) + 1
    while i < len(lista):
        if (lista[i] + 1 == lista[i+1]):
            i += 1
        else:
            return lista[i] + 1