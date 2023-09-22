def intercala(lista1, lista2):
    """Função que dadas duas listas l1 e l2,gera uma l3 intercalando l1 e l2.
    exemplo: entrada l1[2,5,7] e l2[3,6,4];saida l3[2,4,5,6,7]. list,list->list"""
    lista3=lista1+lista2
    return sorted(lista3)