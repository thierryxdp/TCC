def qtd_divisores(numero):
    """funcao divisores que conta quantos divisores um dado
    numero inteiro tem;
    int -> int"""
    
    divisores = []
    i = 2
    while i in range(1,int(numero/2 +1)):
        if numero%i ==0:
            divisores = divisores + [i]
        if numero%i != 0:
            i = i +1
    return len(divisores)