def qtd_divisores(n):
    divi=0
    for i in range(1,n+1):
        if n%i==0:
            divi+=1
    return divi