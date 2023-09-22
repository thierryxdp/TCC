def num_bombons(dinheiro,preco):
    if dinheiro == preco:
        return dinheiro/preco.round()
    elif dinheiro > preco:
        return dinheiro/preco.round()
    else:
        return 0