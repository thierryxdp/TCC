def total(listas,dicionarios):
    '''Função que calcula e  retorna o valor total dos itens da lista que estejam desponíveis na loja.list,dict->float'''
    soma = 0
    for produto in dicionarios:
        if produto in listas:
            soma = soma + dict.get(dicionarios,produto)
    return round(soma,2)