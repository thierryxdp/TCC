def total(lista,dicionario):
    '''Função que me dá como parâmetro uma lista e um 
    dicionário contendo o preço de cada produto da loja.
    E me retorna o valor total dos produtos da lista que 
    tem na loja.
    list, dic -> float'''
    preco=0
    for lista in dicionario:
        if 'lista'=='dicionario':
            preco=preco+dicionario[lista]        
    return round(preco,2)