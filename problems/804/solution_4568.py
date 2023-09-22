def filtra_pares(tupla):
    """Mostra os elementos pares da tupla de elementos inteiros
    tuple -> tuple
    Parameters:
    tupla: Tupla com quatro elementos inteiros 
    Retuns:
    Os elementos pares da tupla de quatro elementos inteiros fornecidos"""
    item1, item2, item3, item4 = tupla
    if item1%2 == 0:
        item1 == True
    else:
    item1= False
    if item 2%2 == 0:
    item 2 == True
    else: 
    item2= False
    item3 = False
    if item 3%2 == 0:
    item3 == True
    else:
    item3 = False 
    if item 4%2 == 0:
    item4 == True 
    else: item4 = False
    pares = filter(None,(item1,item2,item3,item4))
    return (tuple(pares))