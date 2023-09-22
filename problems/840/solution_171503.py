def bolos(A,B,C):
    '''Calcula a quantidadade maxima de bolos que Joao consegue fazer, dados as quantidades de farinh de trigo A, ovo B e leite C'''
    b=((A//2)+(B//3)+(C//5))//3
    if (A<2 or B<3 or C<5):
        b=0
        return b