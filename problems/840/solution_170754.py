def bolos(A,B,C):
    "Retorna o máximo de bolos possíveis de serem feitos com A xícaras de farinha, B ovos e C colheres de sopa"
    MaxA=A//2
    MaxB=B//3
    MaxC=C//5

    return min(MaxA,MaxB,MaxC)