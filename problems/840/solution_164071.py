def bolos(A, B, C):
    ''' retorna quantos bolos podem ser feitos com A xícaras de farinha, B ovos e C colheres de sopa de leite,
    em uma receita que usa uma proporção de 2 xícaras de farinha/3 ovos e 5 colheres de sopa de leite para 
    cada bolo.
    int, int, int --> int'''

    return min(A//2,B//3,C//5)