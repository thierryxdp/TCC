def total(lista,v):
    """recebe uma lista e um dicionário e retorna a soma dos valores do dicionário relacionados ao conteúdo da lista
    list,dict->float"""
    produtos= dict.keys(v)
    valores= dict.values(v)
    r=0

    for x in lista:
        r=r+dict.get(v,x)
    return round(r,2)