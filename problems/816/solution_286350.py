def maiores(lis,n):
    """
assinatura: list, int -> list
"""
    adc= list.append(lis,n)
    org= list.sort(lis)
    ind= list.index(lis,n)
    nli= lis[ind+1::1]
    return nli