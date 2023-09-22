import math
def carros(pessoas,assentos=5):
    """Calcula o número de carros necessários para transportar
    um grupo de pessoas. O núemro padrão de assento é 5.
    Caso os veículos utilizados sejam de capacidade não 
    convencional, deverá ser especificado no segund parâmetro;
    entrada: int
    saída: int"""
    return math.ceil(pessoas/assentos)