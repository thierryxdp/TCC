def qtd_divisores(n):
    divisores=0
    for i in n:
        if n%i==0:
            divisores+=1
    return divisores