def bolos(A,B,C):
    """calcula quantos bolos se consegue fazer.
    int,int,int->int"""
    return min(A//2, B//3, C//5 )