def bolos(A,B,C):
    """ retorna a quantidade de bolos que João consegue fazer,
    sendo A a quantidade de xícaras de farinha de trigo, B
    a quantidade de ovos e C a quantidade de colheres de sopa
    de leite; int , int , int --> int"""
    return min((A/2),(B/3),(C/5))