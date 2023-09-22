# ----------- Receita: -------------
#
# A - 	2 xícaras de farinha    		
# B - 	3 ovos							
# C - 	5 colheres de sopa de leite		
#
#		Só medidas exatas.



def bolos(A,B,C):
	Aposs = A//2
	Bposs = B//3
	Cposs = C//5
	P = (Aposs, Bposs, Cposs)
	#Bolos possíveis:
	BPs = min(P)
	return BPs