def bolos(A,B,C):
    '''Calcula a quantidade de bolos possíveis que podem ser feitos dadas as quantidades obtidas de ingredientes A (xícaras de farinha de trigo), B (ovos), C (colheres de sopa de leite); int, int, int -> int'''
    a=A/2
    b=B/3
    c=C/5
    return min(a,b,c)