def bolos(a,b,c):
    '''funcao que retorna a quantidade maxima de bolos que podem ser feitas para quantidades de ingredientes dispnivel
       float, float ->float'''
    return min(a//2,b//3,c//5)