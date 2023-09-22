def acima_da_media(L):
    import math
    list.sort(L)
    #----------
    LN = len(L)
    SN = sum(L)
    DV = SN/LN
    DV = DV +0.1 
    DV = math.ceil(DV) #Valor(5)/6
    #-------------
    if DV in L:
        IND = list.index(L,DV)
        return L[IND:]
    elif DV not in L:
        DV + 1
        IND = list.index(L,DV)
        return L[IND:]