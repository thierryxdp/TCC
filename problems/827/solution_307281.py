def qtd_divisores(numero):
    """funcao divisores que conta quantos divisores um dado
    numero inteiro tem;
    int -> int"""
    
    divisores = []
    i = 2
    numero = num
    while i in range(1,int(numero/2 +1)):
        if num%i ==0:
            num = num/i
            if i not in divisores:
                divisores = divisores + [i]
        if num%i != 0:
            i = i +1
    return len(divisores)