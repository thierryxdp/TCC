def fatorial(n):
    """Dado um número 'n' a função calcula o fatorial desse número;
    int -> int"""
    i = 1  
    n_fat = 1
    while i <= n:
        n_fat = n_fat*i 
        i = i + 1
    return n_fat