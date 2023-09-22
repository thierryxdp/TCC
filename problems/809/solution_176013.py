def intercala(lista1, lista2):
    """ Dadas duas listas L1 e L2, retorna uma nova lista, L3, coms os elementos de L1 e L2 intercaldos;
    lista,lista->lista """
     L3=lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]
    return L3