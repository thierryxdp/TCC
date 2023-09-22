def filtraMultiplos(lista,n):
    '''funcao que recebe uma lista e um número n como parâmetro  e retorna uma nov lista com apenas os elementos que forem divisíveis por n;
    list, int -> list'''
    l = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo] % n ==0:
            l = l + [lista[proximo],]
        proximo = proximo + 1
    return l