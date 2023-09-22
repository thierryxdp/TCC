def num_bombons(preco, dinheiro):
    quantidade = 0
    while(dinheiro>preco):
        dinheiro = dinheiro - preco
        quantidade = quantidade ++
    return quantidade;