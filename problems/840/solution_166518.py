from math impor floor

def bolos(a,b,c):
    '''funcao que retorna a quantidade maxima de bolos que podera ser obtida a partir
    das quantidades de ingredientes a,b,c, indicando respectivamente xıcaras de farinha de trigo, 
    ovos e colheres de sopa de leite, sendo consideradas apenas as medidas exatas indicadas na receita que somam 10
    int,int,int -> int'''
    return floor(a+b+c)/10