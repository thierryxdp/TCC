def qtd_divisores(n):
    vezes=0
    for i in range(2,n+1) :
        if i%n:
            vezes+=1
    return vezes