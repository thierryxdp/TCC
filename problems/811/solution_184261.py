def colchao (medida ,H,L):
    """Essa função iráretornar se o colchão passará ou não pela porta ; lista -> booleano"""
    list.sort(medida,reverse= True)
    if ((medida[0] > H and medida[1]>L) and (medida[1]> H and medida[0]>L)):
        return False
    else:
        return True