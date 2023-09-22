#
#
#
#
def filtraMultiplos(lista,n):
    i=0
    divisiveis_por_n = []
    while i < len(lista):
        if lista[i]%n!=0:
            i=i+1
            divisiveis_por_n = divisiveis_por_n + lista[i]
        return lista