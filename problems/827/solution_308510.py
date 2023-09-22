def qtd_divisores(n):
    vezes=0
    for i in range(1,n+1) :
        if n%i==0:
            vezes+=1
    return vezes