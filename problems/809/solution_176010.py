def intercala(lista1, lista2):
    """essa função recebe duas listas com 3 elementos cada e retorna uma nova lista contendo os elementos das duas primeiras intercaladas;
    list,list-->list"""
    return[*sum(zip(lista1,lista2),())]