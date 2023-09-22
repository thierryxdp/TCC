def qtd_divisores(n):
    d=0
    for i in range(len(n)):
        if n%i==0:
            d=i
        elif n== -n and n==0:
            d=0
         
    return d