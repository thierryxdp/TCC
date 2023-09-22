def filtraMultiplos(lista, n):
    '''funcao para filtrar os multiplos de um numero n;
    list, int -> list'''
    lista_divisiveis = ()
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
            lista_divisiveis = lista_divisiveis + (lista[i],)
            i = i + 1
            return list(lista_divisiveis)