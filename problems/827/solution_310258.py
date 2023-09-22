def qtd_divisores(numero):
    divisores=list(range(1,numero+1))
    soma=0 
    for x in divisores:
        if numero%x==0:
            soma+=1
    return soma