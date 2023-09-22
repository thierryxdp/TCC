def intercala(lista1, lista2):
    """Funcão recebe duas listas e as retorna alternadas em uma terceira lista"""
    lista3 = [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]
    return lista3