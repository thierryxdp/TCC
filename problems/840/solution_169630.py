def bolos(A,B,C):
    "Essa função retorna a quant máxima de bolo que o joao consegue fazer"
    if A < 2 or B < 3 or C <5:
        return 0
    else:
        return (A+B+C)//10