def fatorial(n):
    """retorna a fatorial do numero n"""
    """int -> int"""
    if n == 0:
        return 1
    else:
        i = 1
        f = n
        while i < n:
            f = f*((n-i)*i)
            i = i + 1
        return f