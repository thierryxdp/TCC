def filtraMultiplos(l,n):
    """Filtra múltiplos do número n na lista l, retorna 
    uma lista dos múltiplos de n na lista l.
    list, int->list"""
    lista=''
    i=0
    while i<len(l):
        if int(l[i])%n==0:
            list.append(lista,l[i])
            i+=1
    print lista