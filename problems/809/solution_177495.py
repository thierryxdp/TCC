def intercala(lista1, lista2):
    """recebe duas listas e retorna uma terceira lista intercalando os valores das listas anteriores"""
    lista3 = lista1[0::1] + lista2[0::1]
    return lista3