def bolos(A,B,C):
    '''retorna a quantidade de bolos que podem ser feitas com base na
    quantidade de xícaras de farinha de trigo A, ovos B e colheres de
    sopa de leite C.'''
    d=A//2
    e=B//3
    f=C//5
    return min(d,e,f)