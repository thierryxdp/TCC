def filtraMultiplos(lista,n):
    '''retorna outra lista com os números multiplos de n da outra lista
    list,int -> list'''
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            list.append(multiplos,lista[proximo])
        proximo = proximo + 1
    return multiplos