def bolos(A, B, C):
    ''' calcula a quantidade máxima de bolos que João consegue fazer, considerando
    "A" a quantidade em xícaras de farinha, "B" a quantidade de ovos e "C" a quantidade 
    de leite em colheres de sopa'''
    return min(A//2, B//3, C//5)