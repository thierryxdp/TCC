def faltante(n):
    x=0
    a=1
    s=2
    list.sort(n)
    while s!=a:
    	a=n[x-1]
    	s=n[x]
        x=x+1
    return x-1