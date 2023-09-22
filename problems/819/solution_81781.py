def filtraMultiplos(lista_num, n):
    '''Filtra os múltiplos de um número n numa lista, list, int -> list'''
    multiplos = []
    i=0
    while i<len(lista_num):
        if lista_num[i]%n==0:
            list.append(multiplos,lista_num[i])
            i=i+1
        else:
            i=i+1
    return multiplos