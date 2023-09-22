# 2 xícaras de farinha 
#3 ovos 
#5 colheres de sopa de leite
#comandos a,b,c 
def bolos(A,B,C):
    '''
    dadas as quantidades dos ingredientes
    para fazer bolo, a função calcula 
    e retorna o numero maximo de bolos que Joao 
    consegue fazer usando as medidas exatas
    dos ingredientes.
    A = xicaras de farinha 
    B = Ovos 
    C = colheres de sopa de leite 
    int, int, int 
    return -> int 
    '''
    return ((A//2)*(B//3)*(C//5))