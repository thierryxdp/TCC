def filtraMultiplos(lista,n):
    """essa funcao recebe uma lista e um numero e filtra na lista os numeros que sao divisiveis por n
    list -> list"""
    multiplos = []
    for x in range(len(lista)):
        if lista[x]%n == 0:
            multiplos.append(lista[x])
    return (multiplos)