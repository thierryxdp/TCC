def bolos(A,B,C):
    """A=numero de xicaras de farinha, B=ovos,C=colheres de sopa
    de leite que joao tem em casa. Sao necessarios no min
    2,3,5 para fazer 1 bolo int,int,int->int"""
    if (A>=2) and (B>=3) and (C>=5): 
        A=A//2
        B=B//3 
        C=C//5
        return min(bolos(A,B,C))
    else:
        return 0