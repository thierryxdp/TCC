def bolos(A,B,C):
    """calcula quantos bolos podem ser feitos dadas as quantidades de farinha, ovos e leite. 
    A,B,C - int,int,int -> int"""
    return min(A//2,B//3,C//5)