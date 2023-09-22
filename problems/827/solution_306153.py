def qtd_divisores(num):
    """Função que calcula a quantidade de divisores que um numero tem,int-->int"""
     
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            yield i 
            outro_divisor = num // i
            if outro_divisor != i: 
                return outro_divisor 
    return num