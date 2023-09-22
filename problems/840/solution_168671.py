def bolos(A,B,C):
    """Função que determina os bolos que podem ser feitos dados os devidos ingredientes"""
    """A=xícaras de farinha de trigo, B=ovos,C=colheres de sopa de leite"""
    """int,int,int -> int"""
    A = A / 2
    B = B / 3
    C = C / 5
    if A <= B and A <= C:
        return A
    elif B <= A and B <= C
		return B
	else:
        return C