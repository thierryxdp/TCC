import math
def bolos(A,B,C):
    '''Calcula e retorna o número maximo de bolos que podem ser feitos dados os parametros A, B e C. int -> int '''
	return math.floor((2*A+3*B+5*C)/10)