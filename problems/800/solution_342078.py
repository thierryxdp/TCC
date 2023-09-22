def total(lista,dicionario):
    '''Função que retorna o valor total dos itens da lista que estejam desponíveis na loja.'''
    '''list,dict->float'''
    soma = 0
    for produto in dicionario:
        if produto in lista:
            soma = soma + dict.get(dicionario,produto)
    return round(soma,2)