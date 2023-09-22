def total(lista,dicionario):
    '''Função que me dá como parâmetro uma lista e um 
    dicionário contendo o preço de cada produto da loja.
    E me retorna o valor total dos produtos da lista que 
    tem na loja.
    list, dic -> float'''
    preco=0
    soma=()
    for lista in dicionario:
        preco=preco+dicionario[lista]
        soma=preco
    return round(soma,2)