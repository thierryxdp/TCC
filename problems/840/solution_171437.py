def bolos(A,B,C):
    '''retorna a quantia máxima de bolos que podem ser feitos seguindo a receita de 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite tendo-se A xícaras de farinha, B ovos e C colheres de sopa de leite'''
    return min(A//2,B//3,C//5)