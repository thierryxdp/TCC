def filtraMultiplos(lista,n):
    '''recebe como entrada uma lista de ńumeros e um numero N, e retorna
outra lista contendo todos os elementos da lista original que forem diviśıveis por n.'''
    i=0
    nova_lista = []
    while i<len(lista):
        if lista[i]%n==0:
           list.append(nova_lista,lista[i])
        i=i+1
    return nova_lista