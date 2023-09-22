def total(lista, dicti):
    """
    Calcula o valor de uma compra baseada numa lista de itens
    lst -> float
    """

    l = []
    k = list(dicti.keys())

    for i in range(len(lista)):
        for j in range(len(dicti)):
            if lista[i] == k[j]:
                l.append(dicti[k[j]])
    
    return round(sum(l), 2)

    #produtos = {'amaciante':4.99, 'arroz':10.90, 'biscoito':1.69, 'cafe':6.98, 'chocolate':3.79, 'farinha':2.99 }; total(['biscoito', 'chocolate', 'farinha'], produtos) -> 8.47