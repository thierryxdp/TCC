def total(lista,dic):
    a=0
    for i in lista:
        a+=dic[i]
    return (round(a,2))