def divisores(n):
    contador=[]  
    for i in range(1,n+1):
        if (n % i) == 0:
            return i
    while contador <= n:
        if num%2==1:
            contador=contador+1
    return n