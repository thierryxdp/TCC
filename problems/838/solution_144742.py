def num_bombons(dinheiro_total, preco):
    return math.floor(dinheiro_total/preco), dinheiro_total - math.floor(dinheiro_total/preco) * preco