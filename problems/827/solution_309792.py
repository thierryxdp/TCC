def qtd_divisores(n):
    "funcao que recebe um número n de entrada e retorna a quantidade de divisores que esse número tem;
    int -> int" 
    divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divisores += 1
        i += 1
    return divisores