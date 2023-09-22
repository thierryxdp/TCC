#%%
def total(lista,produtos):
    """doc"""
    tot = 0
    for produto in lista:
        if produto in produtos:
            tot += produtos[produto]
    return round(tot, 2)