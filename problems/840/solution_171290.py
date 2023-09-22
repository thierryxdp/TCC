def bolos (A,B,C):
    """ calcule e retorne a quantidade de bolos que Joao consegue fazer, sendo A representa a quantidsade de xicaras de fatinhos, B ovos e C colheres de sopa de leite."""
    import math
    b = math.floor (A/2 + B/3 + C/5)
    return b