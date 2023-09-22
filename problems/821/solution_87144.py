def fatorial(numero):
    """Função calcula o fatorial de um número dado
       Parametro: int -> int"""
    soma = 1 
    for x in range(1,numero+1):
        soma = soma * x
    return soma