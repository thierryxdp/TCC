def faltante(x):
    n=len(x)-2
    while n>=0:
        if x[len(x)-1]==x[n]-1:
        	n=n-1
        else:
            return x[n]