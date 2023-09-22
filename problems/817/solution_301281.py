def acima_da_media(lis):
    """
"""
    org= list.sort(lis)
    med= sum(lis)/len(lis)
    nli= lis[round(med)+1::1]
    return nli