def filtraMultiplos(lista,n):
    '''Dado de entrada uma lista de numeros e um numero n, retorna outra
lista lista com todos os elementos da lista original divisiveis por n.
list, int -> list'''
    i=0
    divisiveis=[]
    while i<len(lista):
        if lista[i]%2==0:
            list.append(divisiveis,lista[i])
        i=i+1
    return divisiveis