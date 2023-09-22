def fatorial(n):
    """ função tem como entrada numero N e retorna o fatorial dele"""
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat