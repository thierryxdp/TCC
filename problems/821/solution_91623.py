def fatorial(num):
    """retorna o fatorial de um numero qualquer
    int -> int"""
    i, fat = 0, 1
    while i < num:
        fat += i*fat
        i += 1