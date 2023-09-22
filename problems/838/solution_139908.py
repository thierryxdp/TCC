def comprar():
    print('Compra efetuada')
    return 1

def num_bombons(preco, dinheiro):
    q = 0
    while(dinheiro>=preco):
        dinheiro = dinheiro - preco
        q = q + comprar()
    print('Total de bombons e {}'.format(q))
    return q

num_bombons(3,10)