def filtraMultiplos(lista,n):
    '''Recebe uma lista de numeros e um numero inteiro e retorna quais numeros dentro da lista sao divisiveis por aquele numero inteiro
    list,int->list'''
    multiplos= []
    i=0
    while i<len(lista):
        if lista[i] % n == 0:
           list.append(multiplos,lista[i])
        i= i + 1
    return multiplos