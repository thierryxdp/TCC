def filtraMultiplos(l,n):
    '''
    retorna quais numeros da lista sao multiplos
    list, int -> list
    '''
    lista=[]
    i=0
    while i<len(l):
        if l[i]%n==0:
            lista.append(l[i])
        i=i+1
    return lista