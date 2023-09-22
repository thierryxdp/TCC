def acima_da_media(L):
    import math
    list.sort(L)
    LN = len(L)
    SN = sum(L)
    DV = SN/LN
    DV1 = math.ceil(DV)
    IND = list.index(L,DV1)
    L[IND:]