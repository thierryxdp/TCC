#
#
#
#
def repetidos(lista):
    i=0
    n_vezes=0
    while i < len(lista):
        if lista[i+1]==lista[i]:
            n_vezes=n_vezes+1
    i=i+1
    return n_vezes