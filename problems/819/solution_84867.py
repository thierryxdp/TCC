def filtraMultiplos(x,n):
    soma=[]
    i=0
    while i<len(x):
        if x[i]%n==0:
        soma.append(x[i])
        i=+1
    return soma