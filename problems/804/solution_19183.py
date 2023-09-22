def filtra_pares(tupla):
    """Função que recebe uma tupla com quatro elementos
    inteiros como parâmetro, e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original,
    na mesma ordem em que se encontravam.
    tuple -> tuple"""
    a, b, c, d = tupla 
    pares = ()
   
    if a % 2 == 0:
        pares + (a,)
    if b % 2 == 0:
        pares + (b,)
    if c % 2 == 0:
        pares + (c,)
    if d % 2 == 0:
        pares + (d,)