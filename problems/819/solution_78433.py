def filtraMultiplos(lista,n):
    """Função que dada uma lista de números(lista) e um número (n), retorna outra
    lista contendo os elementos da 'lista' original que forem divisíveis por 'n';
    list, int -> list"""

    multiplos = list()
    num_elementos = len(lista)
    indice = 0

    while indice < num_elementos:
        if (lista[indice] % n == 0):
            list.append(multiplos,lista[indice])

        indice += 1

    return multiplos