def bolos(A,B,C):
    '''calcula o máximo de receitas que podem ser feitas com A quantidades de xícaras de farinha de trigo, B ovos e C colheres de sopa de leite'''
    max_farinha = A//2
    max_ovos = B//3
    max_leite = C//5
    return min(max_farinha, max_ovos, max_leite)