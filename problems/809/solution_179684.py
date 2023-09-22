def intercala(lista1, lista2):
    """função que intercala duas lista formando uma terceira
    com elementos das outras
    entrada: lista1,lista 2:list
    saida:lista
    """
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]