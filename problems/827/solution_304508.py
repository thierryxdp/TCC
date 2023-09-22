def qtd_divisores(n):
    lista1=0
    for divisor in range (1,n+1):
        if n % divisor ==0:
            lista1+=1
return lista1