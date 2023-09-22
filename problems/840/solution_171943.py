def bolos(A,B,C):
    """Calcula o numero máximo de bolos que podem ser produzidos a partir da quantidade de ingredientes presentes na receita e aqueles que possui em casa.
Os parametros são: A (xicaras de farinha de trigo),B (ovos) e C (colheres do sopa de leite). O retorno será um numero inteiro independente da entrada.""" 
    a=A//2
    b=B//3
    c=C//5
    d=min(a,b,c)
    return d