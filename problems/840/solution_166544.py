def bolos(a,b,c):
    '''funcao que retorna a quantidade maxima de bolos que podera ser obtida a partir
    das quantidades de ingredientes a,b,c, indicando respectivamente xıcaras de farinha de trigo, 
    ovos e colheres de sopa de leite, sendo consideradas apenas as medidas exatas indicadas na receita
    int,int,int -> int'''
    return min((a//2),(b//3),(c//5))