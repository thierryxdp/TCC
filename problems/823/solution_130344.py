def faltante(L):
    '''descobre qual número está faltnado numa lista de inteiros de 1 a n
    lista->int'''
    i=1
    while i<=len(L):
        if i!=L[i-1]:
            return i
        i+=1
    return len(L)+1