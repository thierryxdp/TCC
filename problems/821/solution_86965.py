def fatorial(n):
    """função que retorna o fatorial do número n
    int -> int"""
    contrapeso = 1
    produto = n
    num = n
    while contrapeso < n:
        produto = produto*(num - 1)
        num = num - 1
        contrapeso += 1
    return produto