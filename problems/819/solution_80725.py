def filtraMultiplos(numeros,n):
    '''Uma função para filtrar os múltiplos de um numero n.
    e recebe como entrada uma lista de numeros e um numero,
    e retorna outra lista contendo todos os elementos 
    da lista original que forem divisıveis por n. list,int -> list'''
    multiplos = numeros
    multiplos=[]
    i=0
    while i<len(numeros):
        if numeros[i] % n == 0:
            multiplos.append(numeros[i])
        i=i+1
    return multiplos