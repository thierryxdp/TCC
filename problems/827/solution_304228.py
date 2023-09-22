def qtd_divisores(n):
    soma = 1
    if n<0:
            return 0
    for i in range(1,int(n)):
        if n%i==0:
            soma +=1
    return soma