def bolos(A,B,C):
    '''calcula a maior quantidade inteira de bolos que é possível ser feita com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite.
    int, int, int --> int.'''
    return min((A//2),(B//3),(C//5))