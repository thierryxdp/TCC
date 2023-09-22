def fatorial(num):
    """Calcula e retorna o fatorial de um numero(num);
    int --> int"""
    i=0
    factorial=1
    while i < num:
        factorial = factorial * num
        i=i+1
    return factorial