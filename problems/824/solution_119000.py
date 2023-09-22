def uppCons (s):
    sn = ""
    for e in s:
        if e not in "AEIOUaeioÃÕÁÉÍÓÚãõáéíóúÂÊÎÔâêîôû":
            M = str.upper (e)
            sn= sn + Mu
        if e in "AEIOUaeiouÃÕÁÉÍÓÚãõáéíóúÂÊÎÔâêîôû":
            sn= sn + e
    return sn