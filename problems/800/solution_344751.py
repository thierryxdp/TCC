def total(lista, produtos):
    var=0
    for e in lista:
        var+=produtos[e]
    return round (var, 2)