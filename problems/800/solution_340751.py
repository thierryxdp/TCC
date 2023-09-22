def total(lista,produtos):
    '''...'''
    
    produtos={}
    
    for produto in produtos:
        if produto in lista:
            produtos=produtos+1
    return produtos