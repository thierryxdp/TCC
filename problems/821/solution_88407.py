def fatorial(n):
    """Função que dado um número cálcula
    o fatorial deste número. int -> float"""
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat