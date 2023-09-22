def filtraMultiplos(x,n):
    soma=[]
    i=x[0]
    y=0
    while i <=len(x):
        if i%n==0:
            soma.append(i)
        i=x[y] 
        y+=1
    return soma