def filtra_multiplos(lista,n):
    ''' função que recebe uma lista e um número e retorna uma nova lsta contendo apenas os multiplos de n; list;int->list''' 
    c=0
    l1=[]
    while c<len(lista):
        if lista[c]%n==0:
            list.append(l1,lista[c])
        c=c+1
    return l1