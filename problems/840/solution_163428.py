from math import floor
def bolos(a,b,c):
    '''função retorna o número máximo de bolos que João pode fazer com a quantidade "a" de xícaras de farinha de trigo, "b" de ovos e "c" de colheres de sopa de leite
    	int, int, int -> int'''
    return min(a/2, b/3, c/5)