def fatorial(n):
    """Função que recebe um número, 
    calcula e retorna o valor de seu fatorial
    int -> int"""
    controle = n
    while controle > 1:
        n = n*(controle-1)
        controle -= 1
    return n