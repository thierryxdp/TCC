def carros(x,y=5):
    import math
    """Função que retorna a quantidade necessária de carros para uma viagem, dado como parâmetro a quantidade de pessoas. Entrada -> int; Saída -> int"""
    return math.ceil(x/y)