'''Programa calcula a quantidade mínima de bolos que é possível fazer
com base na quantidade de ingredientes, seguindo a proporção 
2:3:5 de xícaras de farinha de trigo, ovos e colheres de sopa de leite, respectivamente.
int, int, int -> int'''
def bolos(A, B, C):
	if A >= 2 and B >= 3 and C >= 5:    
    	AA = A//2
    	BB = B//3
    	CC = C//5
    	if AA < BB and CC:
        	return AA
    	if BB < CC and AA:
        	return BB
    	if CC < AA and BB:
        	return CC
        if AA == BB == CC:
            return A//2
    else:
            return 0