# Dados uma matriz mat de números inteiros e um inteiro num, esta função conta e 
# retorna quantas vezes num aparece na matriz em questão.
# int, list(list) -> int

def conta_numero(num, mat):
    cont = 0
    
    for i in range(len(mat)):
    	for j in range(len(mat[0])):
        	if mat[i][j] == num:
            	cont +=1
	return cont