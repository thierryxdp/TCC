# A função recebe um número e retorna o valor do fatorial desse número
# int->int
# fat: fatorial do número dado
#
def fatorial(n):
    i=0
    fat=1
    while i < n:
        fat=fat*(n-i)
        i=i+1
    return fat