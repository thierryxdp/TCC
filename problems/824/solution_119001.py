def uppCons (s):
    sn = ""
    for e in s:
        if e not in "AEIOUaeiouÃÕÁÉÍÓÚãõáéíóúÂÊÎÔâêîôû":
            M = str.upper (e)
            sn= sn + M
        if e in "AEIOUaeiouÃÕÁÉÍÓÚãõáéíóúÂÊÎÔâêîôû":
            sn= sn + e
    return sn