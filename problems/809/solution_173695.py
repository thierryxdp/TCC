def intercala(lista1, lista2):
    """Recebe duas listas e intercala seus elementos em uma nova lista"""
    lista3 = [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]
    return lista3