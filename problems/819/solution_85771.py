def filtraMultiplos(lista,n):
    """funcao que recebe uma lista e um numero e filtra na lista os numeros que sao divisiveis por n
    list -> list"""
    multiplos = []
    for i in range(len(lista)):
        if lista[i]%n == 0:
            multiplos.append(lista[i])
    return (multiplos)