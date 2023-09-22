def filtraMultiplos(l,n):
    '''a seguinte função retorna uma sublista da lista dada, apenas com os divisiveis de "n".list,float->list'''
    i=0
    nova = list()
    while i<len(l):
        m=l[i]%n
        if m==0:
            list.append(nova,l[i])
        i+=1
    return nova