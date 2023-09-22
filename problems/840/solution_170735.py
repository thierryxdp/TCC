def bolos(A,B,C):
    """Funcao que calcula a quantidade maxima de bolos que podem ser feitos dados os ingredientes"""
    if ((C<5) and (B<3) and (A<2)):
        return 0
    elif((C==5) and (B==3) and (A==2)):
         return 1
    elif ((A>=2) and (B>=3) and (C>=5)):
        return ((A//2)and (B//3)and(C//5)