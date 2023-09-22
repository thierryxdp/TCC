def fatorial(num):
    """Calcula e retorna o fatorial de um numero(num);
    int --> int"""
    i=1
    factorial=1
    while i <= num:
        factorial = factorial * i
        i=i+1
    return factorial