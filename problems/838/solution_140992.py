def num_bombons(preco, saldo):
    '''O número de bombons que Pedrinho pode comprar se dá
    pela quantidade de dinheiro que ele tem dividida pelo preço
    individual dos bombons.'''
    quantidade = saldo // preco
    return quantidade