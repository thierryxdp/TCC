def filtraMultiplos(lista,n):
    '''Dado de entrada uma lista de numeros e um numero n, retorna outra
lista lista com todos os elementos da lista original divisiveis por n.
list, int -> list'''
    i=0
    divisiveis=[]
    while i<len(lista):
        if n%lista[i]==0:
            divisiveis=divisiveis+lista[i]
            i=i+1
        return divisiveis