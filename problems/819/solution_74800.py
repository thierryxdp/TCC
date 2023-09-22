def filtraMultiplos(lista,n):
    """funcao que retorna uma nova lista contendo os elementos da lista de entrada divisiveis por n;
    list,int -> list"""

    multiplos = []
    indice = 0

    while indice < len(lista):

        if lista[indice] % n == 0:
            multiplos = multiplos + 1ist.append(lista[indice])

        indice = indice + 1

    return multiplos