def colchao (medida ,H,L):
    """Essa função iráretornar se o colchão passará ou não pela porta ; lista -> booleano"""
    list.sort(medidas,reverse= True)
    if ((medidas[0] > H and medidas[1]>L) and (medidas[1]> H and medidas[0]>L)):
        return False
    else:
        return True