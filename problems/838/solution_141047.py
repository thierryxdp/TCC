import math
def num_bombons(d,p):
    """Tem a finalidade de calcular quantos bombons pedrinho consegue comprar dado a quantidade de dinheiro que ele tem."""
    """ O objetivo é calcular fazendo uma divisão real, todavia aproximando o valor para o maior numero inteiro menor que o valor mostrado."""
    """ Vamos dividir o preço dos bombons (em reais) pela quantidade de dinhairo que ele tem (em reais), de forma que a quantidade de dinheiro que ele tem deve ser superior a 0."""
    return math.floor (d/p)