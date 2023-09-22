def num_bombons(dinheiro,preço):
    quantidade=int(dinheiro//preço)
    troco=(dinheiro%preço)
    return quantidade,troco