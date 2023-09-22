import math
def bolos (A,B,C):
    """Dados como entrada 3 numeros inteiros referentes respectivamente a xicaras de farinha, numero de ovos e numero de colheres de sopa de leite disponiveis, calcula e retorna a quantidade maxima de bolos que é possivel ser confeccionado com esse material, sendo necessario para fazer um bolo, 2 xicaras de farinha, 3 ovos e 5 colheres de sopa de leite"""
    return math.floor((A//2)+(B//3)+(C//5))