def num_bombons(quantia,valor):
    # Retorna um número de bombons que podem ser 
    # comprados dado o preço (valor)
    # de cada bombom e a quantia (quantia) 
    # de que dispõe-se para a compra.
    # A função recebe números inteiros e
    # também retorna números inteiros
    import math
    return math.floor(quantia/valor)