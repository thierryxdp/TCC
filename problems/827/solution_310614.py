def qtd_divisores(numero):
    """função que conta quantos divisores um número tem
    int -> int"""
    divisores=list(range(1,numero+1))
    soma=0
    for x in divisores:
        if numero%x==0:
            soma+=1
    return soma