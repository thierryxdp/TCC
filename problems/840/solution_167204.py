import math
def bolos(A,B,C):
    '''
    calcula e retorna a quantidade máxima de bolos que é possível fazer com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite seguindouma receita que indica que devem ser usadas 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite;
    int, int, int -> int
    '''
	return math.floor(min(A/2,B/3,C/5))