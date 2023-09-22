def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
   
    for divisor in range(1, numero):
        if numero % divisor == 0:
            return divisor