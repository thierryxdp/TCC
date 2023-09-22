import math
def bolos(a,b,c):
    """Retorna o número de bolos dados os valores de entrada a,b e c disponíveis para a receita, sendo xícaras de farinhade trigo, ovos e colheres de leite respectivamente"""
    return min(a//2,b//3,c//5)