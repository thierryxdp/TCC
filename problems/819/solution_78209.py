filtraMultiplos(l,n):
    ''' Função que verifica se há números múltiplos de n na lista,l.
    list, int -> list'''
    i=0
    s=len(l)
    d=[]
    while(i<s):
        if((l[i]%n)==0):
            list.append(d,l[i])
        i=i+1
    return d