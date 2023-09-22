def faltante(L,N):
    '''descobre qual número está faltnado numa lista de inteiros de 1 a n
    lista->int'''
    i=N
    while i<N:
        if i!=L[i]:
            return i
        i+=1
    return