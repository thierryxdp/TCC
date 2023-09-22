def num_bombons(dinheiro,preco):
    if preco > dinheiro:
        return'sem dinheiro suficiente'
    elif preco == dinheiro:
        return '1'
    else:
        return int(dinheiro/preco)