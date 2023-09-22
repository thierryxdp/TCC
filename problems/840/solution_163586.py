def bolos(a,b,c):
    '''Calcula a quantidade de receitas inteiras de bolo 
    que necessita de 2 xicaras de farinha de trigo, 3 
    ovos e 5 colheres de sopa de leite, dadas as quantias
    dos ingredientes xícaras de farianha a, ovoos b, 
    colheres de sopa de leite c
    	int,int,int -> int'''
    return min(a//2,b//3,c/5)