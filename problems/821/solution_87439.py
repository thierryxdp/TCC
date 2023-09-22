#recebe um número
#é necessário que façamos o fatorial deste número, ou seja, multiplicá-lo
#por um número menor que ele mesmo até que chegue a 1
#exemplo: n(n-1)*(n-2)...(1)
def fatorial(n):
    """Recebe um numero e retorna o fatorial dele"""
    i=0
    fatorial=1
    while i < n:
        fatorial=fartorial*(n-i)
        i+=1
    return fatorial