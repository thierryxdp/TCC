def intercala (l1,l2):
    """ dada duas listas 'lista1' e 'lista2' de tamanho 3, forma uma terceira
    lista intercalando os elementos dessas duas.
    list -> list """
    l1 = [l1[0],l1[1],l1[2]]
    l2 = [l2[0],l2[1],l2[2]]
    l3 = [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]
    return l3