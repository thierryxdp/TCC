#
#
#
#
def filtraMultiplos(lista,n):
    i=0
    div_n=0
    while i < len(lista):
        if lista[i]%n==0:
        div_n=lista[i]
        i=i+1
    return div_n