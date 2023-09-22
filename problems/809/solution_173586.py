# Dadas 2 listas (lista1, lista2), esta função gera uma nova lista lista3,
# intercalando os elementos de lista1 e lista2, como no enunciado.
# list, list -> list
def intercala(lista1, lista2):
    lista3 = (len(lista1)+len(lista2))*[0]
    lista3[0:2*len(lista1):2] = lista1
    lista3[1:2*len(lista2)+1:2] = lista2
    return lista3