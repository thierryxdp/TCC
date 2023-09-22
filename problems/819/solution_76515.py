def filtraMultiplos(lista,n):
    m=[]
    p=0
    while proximo<len(lista):
        if lista[p]%n==0:
            m = m+(lista[p],)
            p = p+1
    return m