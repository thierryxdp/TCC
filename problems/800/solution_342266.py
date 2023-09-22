def total(ls,d):
    compra=0
    for item in ls:
        compra= compra + d[item]
    return round(compra,2)