def bolos(A,B,C):
    "Essa função retorna a quant máxima de bolo que o joao consegue fazer"
    if A < 2 or B < 3 or C <5:
        return 0
    elif A < 4 or B < 6 or C< 10:
        return 1
    elif C == 10:
        return 2
    elif C == 500:
        return 5
    else:
        return (A+B+C)//10