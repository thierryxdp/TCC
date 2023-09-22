def fatorial(numero):
    """A função recebe um numero, e retorna o fatorial deste número;
    int -> int"""
    variavel_fatorial = 1
    i = 2
    while i <= numero:
        variavel_fatorial = variavel_fatorial*i
        i = i + 1
    return variavel_fatorial