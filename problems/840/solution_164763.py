import math
def bolos (A,B,C):
    """Calcula com base no número de ingredientes quantos bolos João consegue fazer."""
    """Temos como parâmetro de entrada (tem que ser números inteiros) as xicaras de farinha de trigo, os ovos e as colheres(sopa) de leite."""
    a= math.floor(A/2)
    b= math.floor(B/3)
    c= math.floor(C/5)
    if a>b>=c or b>a>=c or b>=a>c or a==b==c:
        return (c)
    elif b>=c>a or c>b>=a:
        return (a)
    elif  c>=a>b or a>c>b:
        return (b)