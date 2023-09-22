def faltante(x):
    n=0
    while n<len(x)-1:
        if x[n]+1==x[n+1]:
        	n=n+1
        else:
            return x[n]+1