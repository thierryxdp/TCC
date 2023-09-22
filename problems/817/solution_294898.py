def acima_da_media(L):
    import math
    list.sort(L)
    LN = len(L)
    SN = sum(L)
    DV = SN/LN
    DV = DV +0.1
    DV = math.ceil(DV)
    DV = [DV]
    L = L + DV
    list.sort(L)
    IND = list.index(L,DV)
    IND = IND + 1
    return L[IND:]