def intercala(lista1,lista2):
    """dado como parametro duas listas, return uma outra lista intercalando ambas respectivamente; 
    list, list->list""""
    lista1=[1,3,5]
    lista2=[2,4,6]
    return lista3=lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]