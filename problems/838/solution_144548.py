def num_bombons(dinheiro, preco):
    '''
    Essa função retorna o número máximo de bombons que odem ser coprados com dado dinheiro
    se eles custam um dado preco, que deve ser o maior número inteiro menor que dinheiro/preco
    '''
    return math.floor(dinheiro/preco)