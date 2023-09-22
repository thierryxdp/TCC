def faltante(lista):
    """Recebe uma lista de numeros e retorna qual numero esta
    faltando.
    list --> int"""
    i = 0
    list.sort(lista)
    while i < len(lista):
        if lista[i] + 1 == lista[i+1]:
            i += 1
        else:
            return lista[i]