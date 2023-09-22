def num_bombons(dinheiro, preco):
    q = 0
    while(dinheiro>=preco):
        dinheiro = dinheiro - preco
        q = q + 1
    return q