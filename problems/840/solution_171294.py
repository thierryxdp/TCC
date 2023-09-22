def bolos (A,B,C):
    """ calcule e retorne a quantidade de bolos que Joao consegue fazer, sendo A representa a quantidsade de xicaras de fatinhos, B ovos e C colheres de sopa de leite."""
    import math
	a= math.floor (A/2)
    b= math.floor (B/3)
    c= math.floor (C/5)
	return min (a, b, c)