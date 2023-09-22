def fatorial(n):
    """ essa função irá calcular o fatorial de um numero 'n' dado
entrada -> int
saida -> int """
    fat=1
    i = 2
    while i <=n:
        fat = fat*i
        i=i+1
    return fat