def total(lista,produtos):
    s = 0
    for i in lista:
        if [lista[i]] in list(dict.keys(produtos)):
            s += produtos[lista[i]]
        else: 
            s = s
    return s