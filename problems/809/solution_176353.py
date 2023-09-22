def intercala(lista1, lista2):
    """função que alternar os elementos da lista 1 com a lista 2 resultando na lista 3"""
    """list, list -> list"""
    a=list1[0]
    b=list1[1]
    c=list1[2]
    d=list2[0]
    e=list2[1]
    f=list2[2]
    lista1=[a,b,c]
    lista2=[d,e,f]
    lista3=[(list1[0], list2[0], list1[1], list2[1], list1[2], list2[2])]
    return lista3