def carros(p,c=5):
    '''função que calcula o numero de carros com 5 lugares necessários para transportar p pessoas; int,int-->int'''
    if p=0:
        return 0
    else:
        return p//c+1