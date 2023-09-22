def bolos (A,B,C):
    ''' 
    funcao que calcula e retorna a quantidade
    máxima de bolos inteiros que Joao consegue 
    fazer a partir das entradas A(xicaras de farinha), 
    B(ovos) e C(colheres de leite)
    int, int, int -> int
    '''
	return min(A//2,B//3,C//5)