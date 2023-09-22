def filtraMultiplos(lista, n):
    """ Função que calcula os numeros que sao divisivis
    por n dentro da lista. list, int -> list"""
    divisores = []
    i = 0

    while i <len(lista):
        if lista[i] % n == 0:
            
            list.append(divisores, lista[i])

        i = i+1

    return divisores