import math
def bolos (a,b,c):
    '''função que retorna a quantidade máxima de bolos que será possível
fazer a partir da quantidade de xícaras de farinha de trigo (a), da
quantidade de ovos (b) e da quantidade de colheres de sopa de leite (c),
tal que (a) é maior igual a 2, (b) maior igual a 3 e (c) maior igual a 5;
int,int,int->int'''
    return (a+b+c)//10