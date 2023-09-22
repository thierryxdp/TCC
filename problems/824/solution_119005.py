def uppCons (s):
    sn=""
    for e in s:
        if e in "AEIOUaeiouÃÕÁÉÍÓÚãõáéíóúÂÊÎÔÛâêîôû":
            sn=sn+e
        if e not in "AEIOUaeiouÃÕÁÉÍÓÚãõáéíóúÂÊÎÔÛâêîôû":
            M = str.upper (e)
            sn = sn + M

        return sn