#
#
#
#
def faltante(lista):
    n=1
    while n <= len(lista)+1:
        if not n in lista:
            return n
        n=n+1