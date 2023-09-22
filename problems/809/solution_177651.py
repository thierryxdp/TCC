def intercala(lista1, lista2):
    """Função que recebe duas listas e retorna uma tercira lista
    intercalando a lista1 e a lista2.
    list,list->list
    """
    lista3 = lista1 + lista2
    return lista3[1] + lista3[4] + lista3[2] + lista3[5] + lista3[3] + lista3[6]