def num_bombons(preco, dinheiro):
    while(dinheiro=>preco):
        dinheiro = dinheiro - preco
    return dinheiro;