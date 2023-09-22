def total(l, d):
    '''
    A função recebe uma lista de produtos e um dicionario 
    com seus preços em uma loja e retorna o valor total
    da compra dos produtos disponiveis
    '''
    p = 0
    for x in d:
        if x in l:
            p += dict.get(d, x)
    return p