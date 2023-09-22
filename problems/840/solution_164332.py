from math import(floor)
def bolos(A,B,C):
    '''calcula quantos bolos podem ser assados dadas 
    as quantidades de farinha A, ovos B e leite C'''
    return floor(min(A/2,B/3,C/5))