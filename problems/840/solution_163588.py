import math

def bolos(A,B,C):
    '''calcula a quantidade máxima de bolos que João consegue fazer a partir de uma receita de 2 xícars de farinha de trigo (A), 3 ovos (B) e 5 colheres de sopa de leite;
    	int,int,int -> int'''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))