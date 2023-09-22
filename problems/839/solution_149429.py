from math import ceil
def carros(np,cv=5):
    """Calcula e retorna a quantidade de carros necessário para levar um determinado grupo de amigos, sendo que np equivale ao numero de pessoas e cv a capacidade do carro."""
    return ceil(np/cv)