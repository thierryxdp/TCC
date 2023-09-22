#Intercala os valores da lista1 e da lista2 dentro da lista3
def intercala(lista1, lista2):
    """List,List->List"""
    lista3=lista1+lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3