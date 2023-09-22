def num_bombons(dinheiro,preco):
    if preco > dinheiro:
        return'0.0'
    elif preco == dinheiro:
        return '1'
    else:
        return int(dinheiro/preco)