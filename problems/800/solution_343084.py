def total(compras,precos):
    '''
    funcao que recebe uma lista de compras e um dicionario
    com os precos de cada produto disponivel em uma
    determinada loja e retorna o valor total desses itens
    da lista que estao disponiveis na loja
    list,dict->float
    '''
    lista=[]
    for produto in compras:
        if dict.get(precos,produto,0)!=0:
            list.append(lista,dict.get(precos,produto,0))
    return round(sum(lista),2)