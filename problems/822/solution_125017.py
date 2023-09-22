# A função recebe uma lista de números e retorna o número de vezes que um elemento da lista é
# igual ao elemento anterior
# list->int
#
def repetidos(lista):
    i=1
    n_vezes=0
    while i < len(lista):
        if lista[i]==lista[i-1]:
            n_vezes=n_vezes+1
        i=i+1
    return n_vezes