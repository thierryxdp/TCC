def intercala(lista1, lista2):
    """Retorna uma lista que é formada intercalando os elementos das listas que são os parâmetros de entrada;
    list,list->list"""
    return sum(list(zip(lista1,lista2)))