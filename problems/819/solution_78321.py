def filtraMultiplos(lista,n):
    '''Recebe uma lista de números e um número e retorna uma lista de números nova, onde estes números são os números da lista anterior que são multiplos de n. list,int->list'''
    lista2=[]
    i=0
    k=len(lista)
    while i<k:
        a=lista[i]%n
        if a==0:
            lista2=lista2+[lista[i]]
        i=i+1
    return lista2