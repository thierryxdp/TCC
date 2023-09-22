def bolos(a,b,c):
    ''' qauntidade perfeita de bolos possiveis de serem feitos
    seguindo arrisca a receita'''
    return int(min(int(a)/2,int(b)/3,int(c)/5))