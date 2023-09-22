def filtraMultiplos(lista,n):
    '''Função que recebe uma lista e um número e retorna outra lista
    contendo os elementos da lista original que forem multiplos de n.
    list,int->list'''
    elementos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            elementos=elementos+[lista[i]]
        i=i+1
    return elementos