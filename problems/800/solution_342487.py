def total(lista,prd):
    b=[]
    for i in lista:
        b.append(prd.get(lista[lista.index(i)]))
    d=round(sum(b),2)
    return d