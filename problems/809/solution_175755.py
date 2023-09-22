def intercala(lista1, lista2):
    """Retorna uma lista que é formada intercalando os elementos das listas que são os parâmetros de entrada;
    list,list->list"""
    x=zip(lista1,lista2)
    return sum(list(x))