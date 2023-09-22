def fatorial(n):
    
    """Função que calcula o fatorial de um número
    inteiro qualquer. int -> int """
    c = n
    f = 1
    while c > 0:
        f = f * c
        c = c - 1
    return f