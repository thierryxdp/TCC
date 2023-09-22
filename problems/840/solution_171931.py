def bolos(A,B,C):
    """ calcula e retorna a quantidade possível de bolos com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite, sendo que para produzir um bolo A=2, B=3e C=5"""
    return min(A//2,B//3,C//5)