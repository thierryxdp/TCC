#
#
#
#
def faltante(lista):
    i=1
    n=0
    while i < len(lista):
        if lista[i] == lista[i-1]+1:
        i=i+1
        n=n+lista[i]
        return n