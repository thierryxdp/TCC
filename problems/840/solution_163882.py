def bolos(A, B, C):
    """calcula quantos bolos podem ser feitos dados as quantidades de cada ingrediente A, B e C"""
    if ((A/2)=(B/3)=(C/5)):
        return A/2 or B/3  or C/5
    else:
        return max(A/2, B/3, C/5)