def filtraMultiplos(x,n):
j=0
lista=[]
    while j<len(x):
        if x%n==0:
            lista.append(x[j])
        j = j+1
    return lista