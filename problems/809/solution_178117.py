def intercala(lista1:list, lista2:list) ->list:
    """
    recebe duas listas e as retorna intercaladas
    """
    l1=lista1
    l2=lista2
    return [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]