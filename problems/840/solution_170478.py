import math
def bolos(A,B,C):
    '''A = Nº de xícaras'''
    '''B = Nº de ovos'''
    '''C = Nº de colheres de leite'''
    return math.floor(((A/2)+(B/3)+(C/5))//3)
		if( a<2 or b<3 or c< 5):
        return 0