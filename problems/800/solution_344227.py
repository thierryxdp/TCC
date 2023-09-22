def total(l,d):
    '''Função que recebe uma lista de compras e um dicionario contendo o preço de cada profuto disponivel em
    uma loja, e retorna o valor total dos itens da lista que estejam disponiveis na loja
    list, dict-> float'''
    x = 0
    for elem in range(len(l)):
        y = l[elem]
        if y in dict.keys(d):
            x = x + dict.get(d,y)
    return  round(x,2)