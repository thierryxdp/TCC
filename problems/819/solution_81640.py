def filtraMultiplos(lista,n):
    '''Recebe uma lista e um numero e retorna uma lista contendo os elementos da lista original divisiveis por n
    list,int -> list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n ==0:
            list.append(multiplos,lista[i])
        i=i+1
    return multiplos