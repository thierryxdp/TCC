def total(lista,produtos):
    '''Função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível;
    e retorna o valor total dos itens da lista, caso estejam dispon;iveis;
    list, dict -> str'''
    
    dtotal = 0
    i=0
    
    for produto in lista:
        if lista[i] in produtos:
            dtotal = dtotal + produtos.get(lista[i])
            i+=1
    return round(dtotal,2)