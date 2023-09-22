import math
def bolos(A,B,C):
    '''Calcula e retorna o número maximo de bolos que podem ser feitos dados os parametros A, B e C. int -> int '''
	return math.floor(min(A/2,B/3,C/5))