def eh_ordenada(lista):
    if sorted(lista) == lista:
        return ("True,", 'crescente')
    i = 0
    lista1 = lista[:]
    lista1.sort(reverse = True)
    if (lista1 == lista):
        i = 1
        if (i):
            return ("True,", 'decrescente')
    else: 
        return("False", 'desordenada')