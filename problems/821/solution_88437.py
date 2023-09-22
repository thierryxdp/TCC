def fatorial(n):
    """Função que dado um número(n) calcule o fatorial deste número.
    int -> int"""
    fat = 1
    indice = 2
    while indice <= n:
        fat = fat*indice
        indice = indice + 1

    return fat