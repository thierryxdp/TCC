def num_bombons (d,p):
    """calcula a quantidade de bombons que podem ser comprados com um valor d de dinheiro e p de preço do bombom"""
    return mathceil(d/p)