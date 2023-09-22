from math import ceil
def carros(a,b=5):
    """funçao que define o numero de carros necessarios para transportar uma quantidade a de pessoas, em que b é o quantidade de lugares disponiveis"""
    return ceil.(a/b)