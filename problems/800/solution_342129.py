def total(lista,produtos):
    '''Função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível;
    e retorna o valor total dos itens da lista, caso estejam dispon;iveis;
    list, dict -> str'''
    
    dtotal = 0
    
    for produto in lista:
        if lista in produtos:
            dtotal = dtotal + produtos[lista]
        else:
            return dtotal