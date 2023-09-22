def total(lista,produtos):
    '''...'''
    
    dic={}
    for produto in lista:
        if produto in lista[produtos]:
            dic=dic+[produto]
    return dic