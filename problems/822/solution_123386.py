# Dada uma lista de números, esta função retorna o número de vezes que um
# elemento da lisat é igual ao seu anterior nesta mesma lista.
# list -> int

def repetidos(lista):
    cont = 0
    i = 1
    while i<len(lista):
        if lista[i] == lista[i-1]:
             cont = cont +1
        i = i+1
    return cont