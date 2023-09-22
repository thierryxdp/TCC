def bolos(a, b, c):
    """calcula a quantidade maxima de bolos que joao consegue fazer;
    int, int, int -> int"""
    a= a//2
    b= b//3 
    c= c//5
    return min(a,b,c)