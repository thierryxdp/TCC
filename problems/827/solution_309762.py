def qtd_divisores(n):
    """ Função que retorna a quantidade de divisores de 
    um número.
    Entrada: int
    Saída: int """  
    divisores = 0
    for divisor in range(1,n+1):
        if n%divisor == 0:
            divisores = divisores + 1
    return divisores