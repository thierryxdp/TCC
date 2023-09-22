#funcao q calcula o maior numero de bobmbons com o dinheiro q tem dados o dinheiro e o preco do bombom
def num_bombons(dim,preco):
    """calcula a maior quantidade de bombom de acordo com o preco e o dinheiro q se tem
    float,float - int,float"""
    return int(dim/preco),float(dim%preco)