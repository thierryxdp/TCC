def fatorial(numero):
    """funcao que dado um numero natural de entrada, calcula o
    fatorial desse numero;
    int -> int"""
    
    Fatorial = numero
    n = 1
    while n < numero:
        Fatorial = Fatorial * n
        n = n + 1
    return Fatorial