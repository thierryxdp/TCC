def total(lista_compras,produtos):
    '''Recebe uma lista de compras e um dicionario vontendo o preco de cada produto, e retorna o valor total dos itens da lista disponiveis na loja;
    list,dict->float'''
    
    i=0
    valor_total=[]
    
    while i<len(lista_compras):
        if lista_compras[i] in produtos:
            list.append(valor_total,produtos[lista_compras[i]])
        i=i+1
    return sum(valor_total)