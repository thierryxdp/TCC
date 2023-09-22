def total(lista,produtos):
    s = 0
    for i in lista:
        if i in list(dict.keys(produtos)):
            s += produtos[i]
        else: 
            s = s
    return round(s,2)