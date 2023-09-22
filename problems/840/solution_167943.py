def bolos(A,B,C):
    """"Calcula a partir da receita de bolo na qual a proporcao usada e 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite quantos bolos e possivel fazer."""
    a=A//2
    b=B//3
    c=C//5
    return min(a,b,c)