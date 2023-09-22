def intercalar_listas(lista1,lista2):
    """Dado uma duas listas contendo três números reais, intercala seus valores:
    list[int,int,int],list[int,int,int]-->list"""
    l1=[lista1[0],lista1[1],lista1[2]]
    l2=[lista2[0],lista2[1],lista2[2]]
    l3=[l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]
    return l3