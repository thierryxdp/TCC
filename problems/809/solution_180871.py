def intercala(lista1, lista2):
    """
    Essa função, dados duas listas de len = 3, como argumentos, ira retornar uma lista
    com os elementos das duas listas de forma intercalada, ex.: lista1=[1,2,3] lista2=[4,5,6]
    lista que a função ira retornar = [1,4,2,5,3,6]
    list,list->list
    """
    l3 = []
    l3 = list.append(l3,lista1[0]) + list.append(l3,lista2[0]) + list.apend(l3,lista1[1]) + list.append(l3,lista2[1]) + list.append(l3,lista1[2]) + list.append(l3,lista2[2])
 
    return l3