def bolos(A,B,C):
    #Calculo de bolos que podem ser feitos dadoa A(xicaras de farinha), B(ovos),C(colheres de sopa)
    Na=A/2
    Nb=B/3
    Nc=C/5
    N=min(Na,Nb,Nc)
    return math.floor(N)