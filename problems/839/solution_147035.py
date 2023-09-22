from math import ceil
def carros(p, c=5):
    """dado um grupo de p amigos que desejam viajar, e definida a
    capacidade c de pessoas em um veículo, calcula quantos veículos(iguais)
    são necessários para levá-los. Caso c não seja definido, seu valor será 5,
    que é a capacidade de pessoas em um veículo convencional"""
    return ceil(p/c)