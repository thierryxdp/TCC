import math
def bolos(a,b,c):
    '''funçao que calcula a quantidade máxima de bolos que é possível fazer com 'a' xícaras de farinha, 'b' ovos e 'c' colheres de leite, sendo que para fazer um único bolo serão necessarios 2 xicaras de farinha, 3 ovos e 5 colheres de sopa de leite'''
    return min(a//2,b//3,c//5)