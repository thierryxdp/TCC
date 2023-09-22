def filtraMultiplos(lista, n):
    'filtra os multiplos do numero n e os retorna em uma lista'
    'list, int -> list'
    contador = 0
    lista1 = []
    while contador < len(lista):
        if lista[contador]%n == 0:
            list.append(lista1, lista[contador])
        contador = contador + 1
    return lista1