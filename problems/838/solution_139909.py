def num_bombons(preco, dinheiro):
    q = 0
    while(dinheiro>=preco):
        dinheiro = dinheiro - preco
        q = q + 1
    print('Total de bombons e {}'.format(q))
    return q