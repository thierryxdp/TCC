def qtd_divisores(n):
    soma = 1
    for i in range(1,int(n)):
        if n%i==0:
            soma +=1
    return soma