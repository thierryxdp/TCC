def filtramultiplos(lista,n):
    multiplos=[]
    for k in lista:
        if k%n==0:
            multiplos.append(k)
    return multiplos