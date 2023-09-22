def bolos(A,B,C):
    """ retorna a quantidade de bolos a serem feitos de acordo com a receita levando em conta a quantidade de xicaras de farinha de trigo(A), ovos(B), e colheres de sopa(C);
    int,int,int-> int """
    if (A//2) and (B//3) and (C//5)>=1:
        return min((A//2), (B//3), (C//5))
    else:
        return 0