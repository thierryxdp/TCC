from math import ceil

def carros (num,cap=5):
    """retorna o número exato de carros para a viagem dados
    o número de pessoas (num) e da capacidade de transporte (cap). 
    Caso a capacidade não seja dada, considerará cap igual a 5."""
    return ceil (num/cap)