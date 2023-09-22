#
#
#
#
def faltante(lista):
    n=1
    while n < len(lista):
        if not n in lista:
            return n
        n=n+1