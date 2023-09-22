def bolos(A,B,C):
    """cada bolo consome A xícaras, B ovos, e C colheres, retorna o valor minimo de bolos
    int,int,int->float"""
    return min(A//2,B//3,C//5)