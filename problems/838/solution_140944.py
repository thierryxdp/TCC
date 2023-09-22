def num_bombons(dim,preco):
    """calcula a maior quantidade de bombom de acordo com o preco e o 
    dinheiro q se tem, e o valor de troco"""
    return int(dim/preco),float(dim%preco)