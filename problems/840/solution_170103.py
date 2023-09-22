def bolos(A,B,C):
    '''Calcula e retorna a quantidade mínima de bolo que é possível fazer com a quamtidade de ingredientes dado, A para xícaras de farinha de trigo, B para ovos e C para colheres de sopa de leite
    	int,int.int -> int'''
    
    return min(A//2,B//3,C//5)