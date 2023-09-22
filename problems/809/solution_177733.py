# intercala elementos de 2 listas
def intercala(lista1, lista2):
    """retorna uma nova lista com os elementos da lista1 intercalado com os da lista2, int -> int"""
    L1=lista1
    L2=lista2
    L3=L1[0:1] + L2[0:1] + L1[1:2] + L2[1:2] + L1[2:3] + L2[2:3]
    return L3