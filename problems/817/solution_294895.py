def acima_da_media(L):
    import math
    list.sort(L)
    LN = len(L)
    SN = sum(L)
    DV = SN/LN
    DV = DV +0.1
    DV1 = math.ceil(DV)
    IND = list.index(L,DV1)
    IND = IND + 1
    return L[IND:]