def filtraMultiplos(lista,n):
    '''recebe uma lista e um int n para retornar uma nova lista com os valores multiplos de n
    entrada: list, int
    saida: list'''
    divisiveis=[]
    proximo=0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            list.append(divisiveis,lista[proximo]) 
        proximo = proximo + 1
    return divisiveis