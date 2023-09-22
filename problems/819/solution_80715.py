def filtraMultiplos(lista,n):
    '''
    recebe uma lista e um numero n, retorna outra lista 
    contendo todos os elementos da lista original divisiveis
    por n
    list, float->list
    '''
    divisores=[]
    i=0
    while i<len(lista):
        if lista[i]%n == 0:
            list.append(divisores,lista[i])
            
        i=i+1
    return divisores