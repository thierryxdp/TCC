def filtraMultiplos(lista, n):
    '''filtra os numeros da lista n e retorna uma lista apenas com os numeros divisiveis por n
    list, int -> list'''
    i=0
    divisivelLista = []
    while i < len(lista):
        if(lista[i] % n == 0):
            divisivelLista.append(lista[i:])        
        i++
    return divisivelLista