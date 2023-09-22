def filtraMultiplos(lista,n):
    """Sua função retona uma lista contendo todos os elemtnos da lista
    original que forem divisíveis por n.
    list--int-->list"""
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[1]%n == 0:
            list.insert(multiplos,i,lista[i])
    return multiplos