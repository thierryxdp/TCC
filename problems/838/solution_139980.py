from math import round
num_bombons(dinheiro,preço):
    """Essa função calcula o númeor de bombons que Pedrinho pode comprar,
    e como entrada temos o preço e o dinheiro e como saída temos a quantidade de bombons;
    float,float->float"""
    return round(dinheiro//preço)