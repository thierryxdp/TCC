def total(lista,produtos):
    '''A funçaõ recebe uma lista em um dicionario e retorna 
    o valor total dos itens valores do dicionario.
    list,dict->int'''
    
    int=''
    
    for produto in lista:
        if produtos in lista[produtos]:
            int=int+[produtos]
    return int