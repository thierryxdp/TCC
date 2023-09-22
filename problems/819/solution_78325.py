filtraMultiplos(lista,n):
    i=0
    a=[]
    b=len(lista)
    while i<b:
        if lista[i]%n==0:
            a=lista[i]+a
        i=i+1
    return a