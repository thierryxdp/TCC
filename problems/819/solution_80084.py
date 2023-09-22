def filtra_Multiplos(l,n):
    """Dada uma lista "l" e um número "n"
    retorna uma lista com os elementos da lista "l"
    divisveis por n
    list, int -> list"""
    i=0
    dn=[]
    while (i<len(l)):
        if l[i]%n==0:
            list.append(dn,l[i])
        i+=1
    return dn