def total(lista,dicionario):
    '''Função que me dá como parâmetro uma lista e um 
    dicionário contendo o preço de cada produto da loja.
    E me retorna o valor total dos produtos da lista que 
    tem na loja'''
    preco=[]
    for lista in dicionario[lista]:
        preco=preco+[lista]
    return preco