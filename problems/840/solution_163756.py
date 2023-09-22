def bolos(A,B,C):
    '''Calcula a maior quantidade de bolos que podem ser feitos seguindo a receita
       Parametro: A - quantidade de xicaras de farinha disponiveis
                  B - quantidade de ovos disponiveis 
                  C - quantidade de colheres de sopa de leite disponiveis
                  int
        Retorna: A maior quantidade de bolos que é possivel ser feita
                 int'''
    return min (A//2, B//3, C//5)