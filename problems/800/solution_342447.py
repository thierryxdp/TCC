def total(lista,produtos):
    '''list, dict -> float'''
    x=0
    for item in produtos:
        if item in lista:
            x+=dict.get(produtos,item)
    return round(x,2)