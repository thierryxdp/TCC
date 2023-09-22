def total(lista,dici):
    tudo=0
    for item in lista:
        if item in dici:
            tudo=tudo+float(dici[item])
    return tudo