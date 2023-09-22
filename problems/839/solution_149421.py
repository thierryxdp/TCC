def carros(num_pessoas, cap_carros = 5):
    '''A função retorna a quantidade mínima de carros
    a serem utilizados dado um número de pessoas. Caso a
    capacidade do carro seja especificada na última entrada, o programa
    operará com este dado, do contrário, o valor default é 5. A função
    deve receber valores int e devolve obrigatoriamente valores int.'''
    import math
    return math.ceil(num_pessoas/cap_carros)