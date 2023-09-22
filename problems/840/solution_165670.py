import math
def bolos(A,B,C):
    '''calcula a quantidade de bolos que é possível fazer a partir
    da quantidade de ingredientes fornecidos, sendo xícaras de farinha
    de trigo(A), ovos(B) e colheres de sopa de leite(C). A receita para
    a confecção de um bolo é 2A+3B+5c.
    int|float,int|float,int|float-->int'''
    return min((A//2),(B//3),(C//5))