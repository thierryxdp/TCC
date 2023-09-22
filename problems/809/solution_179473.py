def intercala(lista1, lista2):
    """
    
    :lista1->list:
    :lista2->list:
    :return->list:
    """
             
    L1=lista1
    L2=lista2
    L1_2=[lista1[0], + lista2[0], + lista1[1]]
    L2_2=[lista2[1], + lista1[2], + lista2[2]]
    L3= L1_2+L2_2
    return L3