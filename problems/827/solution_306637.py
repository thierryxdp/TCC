def qtd_divisores(n):
    contador=[]  
while contador <= n:
    for i in range(1,n+1):
        if (n % i) == 0:
            return n
        contador=contador+1
    return 0