def repetidos(l):
    ''' Função que conta o numero de elementos repetidos em uma lista.
    list->int'''
    i=0
    n=len(l)
    s=0
    while(i<n):
        if(l[i]==l[(i+1)]):
            s=s+1
        i=i+1
    return s