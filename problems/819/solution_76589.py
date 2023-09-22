def filtraMultiplos(lista, numero):
    """Minha função recebe uma lista e numero, me devolve uma outra lista,
    somente com os multiplos deste numero
    list, int -> list"""
    nova_lista = []
    i = 0
    while i<len(lista):
        if lista[i]%numero == 0:
            list.insert(nova_lista), i, lista[i])
        i = i + 1
        return nova_lista