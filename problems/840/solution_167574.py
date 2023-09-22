def bolos(A,B,C):
""" cada bolo consome 2A xícaras, 3B ovos, e 5C colheres de sopa de leite, retorna a quantidade maxima possivel
int,int,int->float"""
return min(A//2, B//3,C//5)