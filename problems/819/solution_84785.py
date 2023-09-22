def filtraMultiplos(x,n):
    soma=[]
    i=0
    while i %n==0:
        soma.append(i)
        i+=1
    return soma