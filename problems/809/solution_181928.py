def intercala(lista1, lista2):
    """função que realiza a concatenação entre duas listas de 3 elementos de forma untercalada,
    gerando uma terceira lista com 6 elementos;
    list,list->list"""
    lista3= [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]
    return lista3