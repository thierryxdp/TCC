def filtraMultiplos(lista,n):
    '''filtra multiplos de um numero
    list,int->list'''
    multpl=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            multpl.append(lista[i])
        i=i+1
    return multpl