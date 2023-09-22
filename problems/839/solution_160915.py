def carros(p,c=5):
    """Calcula e retorna o número exato de carros necessários
    para uma viagem dados a quantidade de pessoas e a capacidade
    do veículos (para os não convencionais, ou seja, com capacidade
    maior que 5
    int, int -> int"""
    import math
    return math.ceil(p/c)