def bolo(A,B,C):
    """A=numero de xicaras de farinha, B=ovos,C=colheres de sopa
    de leite que joao tem em casa. Sao necessarios no min
    2,3,5 para fazer 1 bolo
    int,int,int->int"""
    bolo1=(2,3,5)
    if A//2>=1:
        if B//3>=1:
            if C//5>=1: 
                return A+B+C=0
            else:
                return 0