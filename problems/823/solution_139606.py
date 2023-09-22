def faltante(x):
    n=len(x)-1
    while n>=0:
        if x[len(x)]==x[n]-1:
        	n=n-1
        else:
            return x[n]