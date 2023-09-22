def filtra_multiplos(lista,n):
    '''funcao que recebe uma lista e um numero e retorna outra lista contendo todos 
    os elementos da lista original que forem divisiveis por n.
    list->list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n == 0:
            multiplos = multiplos + [lista[i]]
        i=i+1
    return multiplos