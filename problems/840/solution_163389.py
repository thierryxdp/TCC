def bolos(A,B,C):
    '''calcula a quantidade de bolos que podem ser feitos dados a quantidade de A de xicaras de farinha de trigo, B de ovos e C de colheres de sopa de leite
    int, int, int => int'''
    n_bolos_A=A//2
    n_bolos_B=B//3
    n_bolos_C=C//3
    return min(n_bolos_A,n_bolos_B,n_bolos_C)