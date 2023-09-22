def colchao(medidas,H,L):
    """ Dado as tres dimençoes do colchao, verificar se o colchão passara pela porta de altuta H e largura L.
    :medidas:list->list
    :H:int->int
    :L:int->int
    :return: bool->bool"""
    [A,B,C] = medidas
    if A and B > H and L:
        return False