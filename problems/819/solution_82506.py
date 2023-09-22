def filtraMultiplos(lista,n):
    """Sua função retona uma lista contendo todos os elemtnos da lista
    original que forem divisíveis por n.
    list--int-->list"""
    i = 0
    nova_lista = []
    while i < len(lista):
        if lista[i]%n == 0:
            list.insert(nova_lista,i,lista[i])
            i += 1
    return nova_lista