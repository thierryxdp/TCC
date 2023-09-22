def carros(p,a=5):
    """calcula a quantidade de carros necessária para 
    comportar um número p de pessoas, com valor a de 
    capacidade, caso nenhum valor seja atribuido a a, 
    será considerado o valor padrão de 5"""
    import math
    return math.ceil(p/a)