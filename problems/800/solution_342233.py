def total(lista,dicionario):
    '''Função que me dá como parâmetro uma lista e um 
    dicionário contendo o preço de cada produto da loja.
    E me retorna o valor total dos produtos da lista que 
    tem na loja.
    list, dic -> float'''
    x=0
    for x in range(len(lista)):
        if lista[x] in dicionario:
            preco=preco+dicionario[lista[x]]            
    return round(preco,2)