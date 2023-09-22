def bolos(A,B,C):
    """Funcao que calcula a quantidade maxima de bolos que podem ser feitos dados os ingredientes"""
    if A>=2:
        return (A//2)
    elif A<2:
        return 0
    elif B>=3:
        return (B//3)
    elif B<3:
        return 0
    elif C>=5:
        return (C//5)
    elif C<5 and B<3 and A<2:
        return 0