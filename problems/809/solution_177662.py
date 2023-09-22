def intercala(lista1,lista2):
    """Função que recebe duas listas e retorna uma tercira lista
    intercalando a lista1 e a lista2.
    list,list->list
    """
    L3 = lista1 + lista2
    return L3[0] + L3[3] + L3[1] + L3[4] + L3[2] + L3[5]