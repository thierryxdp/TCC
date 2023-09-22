def FiltraMultiplos (lista,n):
    '''funçao que recebe como entrada uma lista de numeros e um numero, e retorna outra lista
    contendo todos os elementos da lista original que forem divisiveis por n'''
    listaMultiplos = []
    i=0
    while i<len(lista):
        if lista [1]%n==0:
            listaMultiplos=listaMultiplos + [lista[i]]
        i=i+1
            return listaMultiplos