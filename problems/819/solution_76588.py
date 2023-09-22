def filtraMultiplos(lista,n):
    #Dado uma lista com números e um número, retorna uma nova lista com os múltiplos deste. list,int -> list.
    multiplos =[]
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            list.append(multiplos,lista[proximo])
        proximo = proximo + 1
    return multiplos