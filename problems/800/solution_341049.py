def total(lista,produtos):
    '''A funçaõ recebe uma lista em um dicionario e retorna 
    o valor total dos itens valores do dicionario.
    list,dict->int'''
    
    i=''
    
    for produto in lista:
        if produtos in lista[i]:
            i=i+[produtos]
    return int