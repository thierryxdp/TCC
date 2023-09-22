def qtd_divisores(numero):
    """Função que dado um número inteiro, retorna a quantidade de 
    divisores que esse número possuí.
    int -> int
    """ 
    divisor = 0
    for n in range(1,numero+1):
        if numero%n==0:
            divisor = divisor+1
    return divisor