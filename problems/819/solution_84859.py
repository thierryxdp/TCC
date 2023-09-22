def filtra_multiplos(lista,n):
    '''funcao que recebe uma lista e um numero e retorna outra lista contendo todos 
    os elementos da lista original que forem divisiveis por n.
    list->list'''
    proximo=0
    multiplos=[]
    while proximo<len(lista):
        if lista[proximo]%n == 0:
        else:
             multiplos = multiplos + [lista[proximo]]
        proximo=proximo+1
    return multiplos