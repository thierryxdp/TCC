def intercala(lista1, lista2):
    """recebe duas listas e retorna uma terceira lista intercalando os valores das listas anteriores"""
    lista3 = lista1[0::2] + lista2[0::2]
    return lista3