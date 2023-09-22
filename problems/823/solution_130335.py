def faltante(l,n):
    '''descobre qual número está faltnado numa lista de inteiros de 1 a n
    lista->int'''
    i=1
    while i<n:
        if i!=l[i]:
            return i
        i+=1