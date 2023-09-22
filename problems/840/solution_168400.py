from math import floor
def bolos (a,b,c):
    ''' define a quantidade máxima de bolos que João pode fazer,
    dados os valores das xícaras de farinha de trigo, ovos e 
    colheres de sopa de leite respectivamente'''
    '''int,int,int-->int'''
    nbolos = (a,b,c)/(2,3,5)
    return floor(nbolos)