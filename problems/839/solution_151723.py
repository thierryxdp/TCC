from math import ceil
def carros(x,y=5):
    """Calcula a quantidade de carros necessária para a viagem, sendo x o total de passageiros e y a capacidade de cada carro.
    Quando a entrada y não for dada, considera-se seu valor igual a 5.
    int, int-> int"""
    return ceil(x/y)