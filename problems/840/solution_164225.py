def bolos(A,B,C):
    '''
    A = xicaras de farinha de trigo
    B = ovos
    C = colheres de sopa de leite
    dado o numeros de A,B e C retorna o numero de bolos
    entrada: int,int,int
    saida:int
    '''
    if A<2 or B<3 or C<5:
        return 0
    else:
        return min((A//2,B//3,C//5))