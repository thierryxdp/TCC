#
#
#
#
def faltante(lista):
    i=0
    n=0
    while i < len(lista):
        if lista[i+1]-lista[i]==1:
            i=i+1
            n=n+lista[i]
        return n