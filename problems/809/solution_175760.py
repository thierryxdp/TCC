def intercala(lista1, lista2):
    """Retorna uma lista que é formada intercalando os elementos das listas que são os parâmetros de entrada;
    list,list->list"""
    return list(list(zip(lista1,lista2))[0])+list(list(zip(lista1,lista2))[1])+list(list(zip(lista1,lista2))[2])