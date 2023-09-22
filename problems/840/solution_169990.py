def bolos(A,B,C):
    """Calcula a quantidade máxima de bolos que uma pessoa consegue fazer, a da quantidade de ingredientes que possui: A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite."""
    a=A//2
    b=B//3
    c=C//5
    return min(a,b,c)