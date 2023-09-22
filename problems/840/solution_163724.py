def bolos (A,B,C):
     """Função que calcula a quantidade de bolos que podem ser feitos, considerando uma quantidade "A" de xícaras de farinha, "B" de ovos e "C" de colheres de sopa de leite. Sabe-se também que são necessários 2, 3 e 5 unidades de cada, respectivamente, para fazer cada bolo"""
     return min(A//2,B//3,C//5)