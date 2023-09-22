def qtd_divisores(numero):
    """funcao divisores que conta quantos divisores um dado
    numero inteiro tem;
    int -> int"""
    
    divisores = []
    i = 1
    while i in range(1,numero):
        if numero%i ==0:
            divisores = divisores + [i]
        i = i +1
    return len(divisores)