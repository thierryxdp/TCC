def qtd_divisores(n):
    i=1
    divisores=0
    while i<=n:
        if n%i==0:
        	divisores=divisores+1
    	i=i+1
    return divisores+1