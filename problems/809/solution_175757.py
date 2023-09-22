def intercala(lista1, lista2):
    """Retorna uma lista que é formada intercalando os elementos das listas que são os parâmetros de entrada;
    list,list->list"""
    x=zip(lista1,lista2)
    return list(list(x)[0])+list(list(x)[1])+list(list(x)[2])