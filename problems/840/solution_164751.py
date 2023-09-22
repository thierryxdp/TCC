import math
def bolos(a,b,c):
	'''Calcula a quantidade possivel de bolos dado os ingredientes A(Xícaras) B(Ovos) e C(Colheres de sopa de leite)'''
	A=math.floor(a/2)
	B=math.floor(b/3)
	C=math.floor(c/5)
	if A>B>=C or B>A>=C or B>=A>C or A==B==C:
		return(C)
	elif B>=C>A or C>B>=A:
		return(A)
	elif C>=A>B or A>C>=B:
		return(B)