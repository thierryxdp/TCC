from math import ceil
def bolo(farinha=2,ovo=3,leite=5):
    ''' '''
    a = farinha % 2 == 0
    b = ovo % 3 ==0
    c = leite % 5==0
    return min(a,b,c)