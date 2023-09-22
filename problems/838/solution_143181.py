import math
def num_bombons (dinheiro:int, precobombom:int) -> int:
    '''Retorna o número de bombons que podem ser comprados, dado o preço do bombom e o valor a ser gasto.
    A função math.floor arredonda o valor para baixo, 
    se certificando que o comprador não vai levar um 
    valor quebrado de bombons.'''
    return math.floor(dinheiro/precobombom)