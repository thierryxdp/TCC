def num_bombons(dinheiro,preco):
    """int,int -> int; Função que calcula a quantidade de bombons possiveis de serem comprados a partir de um dada quantia"""
    import math
    return math.floor(dinheiro/preco)