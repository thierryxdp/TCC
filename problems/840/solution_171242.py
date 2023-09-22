import math
def bolos (A,B,C):
    '''calcula a quantidade máxima de bolos que joao consegue fazer, sendo A para xicaras de farinha, B para ovos e C colheres de acucar; 
       int,int->float'''
    return min(A//2,B//3,C//5)