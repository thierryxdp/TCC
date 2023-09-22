def bolos(A,B,C):
    '''função que calcula a quantidade de bolos que uma pessoa consegue fazer dados
    A(xícaras de farinha, B(ovos), C(colheres de sopa de leite)'''
    a=A/2
    b=B/3
    c=C/5
    return min(a,b,c)