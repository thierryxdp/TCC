def intercala(lista1, lista2):
    """recebe 2 listas e retorna uma terceira lista com os elesmentos dados anteriormente intercalados"""
    lista3 = lista1[0::1] + lista2[0::1]
    return lista3