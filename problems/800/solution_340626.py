def total(lista,dicionario):
    '''Recebe uma lista de compras e um dicionário com os preços de
    cada produto e retorna o valor total dos itens da loja que 
    estejam disponíveis
    list,dict->float'''
    comprados=0
    for produto in dicionario and lista:
        comprados=comprados+dict.get(dicionario,produto)
    return comprados