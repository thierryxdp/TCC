import math
def bolos(A,B,C):
    '''A = Nº de xícaras'''
    '''B = Nº de ovos'''
    '''C = Nº de colheres de leite'''
    return math.floor(((A/2)+(B/3)+(C/5))//3)
	if( A<2 or B<3 or C< 5):
       	return 0