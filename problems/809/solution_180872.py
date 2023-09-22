def intercala(lista1, lista2):
    """
    Essa função, dados duas listas de len = 3, como argumentos, ira retornar uma lista
    com os elementos das duas listas de forma intercalada, ex.: lista1=[1,2,3] lista2=[4,5,6]
    lista que a função ira retornar = [1,4,2,5,3,6]
    list,list->list
    """
    nova_lista = []
    l10 = [lista1[0]]
    l20 = [lista2[0]]
    l11 = [lista1[1]]
    l21 = [lista2[1]]
    l12 = [lista1[2]]
    l22 = [lista2[2]]
    nova_lista = l10+l20+l11+l21+l12+l22
 
    return l3