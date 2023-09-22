def bolo(A,B,C):
    """A=numero de xicaras de farinha, B=ovos,C=colheres de sopa
    de leite que joao tem em casas. Sao necessarios no min
    2,3,5 para fazer 1 bolo
    int,int,int->int"""
    A=(A//2)
    B=(B//3)
    C=(C//5)
    bolo=A,B,C
    return bolo