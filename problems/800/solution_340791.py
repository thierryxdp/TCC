def total(lista,produtos):
    '''...'''
    dic={}
    
    for produto in lista:
        if produtos in lista[produto]:
            dic=dic+1
    return dic