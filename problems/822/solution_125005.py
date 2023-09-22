#
#
#
#
def repetidos(lista):
    i=1
    n_vezes=0
    while i < len(lista):
        if lista[i-1]==24:
            return lista[i-1]