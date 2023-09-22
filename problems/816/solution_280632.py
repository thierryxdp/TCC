def maiores(l,n):
    ''' Função que analisa a lista l e devolve apenas os elemento maiores que n
    list,int-> list'''
    t=0
    if(n not in l):
        t=1
        list.append(l,n)
        list.sort(l)
        x=list.index(l,n)
        return l[x:]
    elif((n in l) and t =0):
        list.append(l,n)
        list.sort(l)
        x=list.index(l,n)
        return l[x+1:]