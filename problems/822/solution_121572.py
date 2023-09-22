def repetidos(lista):
    '''Retorna quantas vezes um elemento da lista é igual ao anterior;
    list -> int'''
    i=1
    n=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            n=n+1      
        i=i+1
    return n