def filtraMultiplos(lista,n):
    '''retorna os multiplos de n 
    list, int -> list'''
    i=0
    x=list()
    while i<len(lista):
        if lista[i]%n==0:
            list.append(x,lista[i])
        i+=1
    return x