def qtd_divisores(n):
    tot=0
    for i in range (1,n+1):
        if n % i ==0:
            tot+=1
return tot