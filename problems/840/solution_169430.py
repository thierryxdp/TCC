def bolos (A, B, C):
    '''calcula a quantidade máxima de bolos que consegue fazer com
 A xicaras de farinha de trigo, B ovos e C colheres de sopa de leite.'''
    '''int, int, int = int'''
    farinha = A/2
    ovos = B/3
    leite = C/5
    return min(farinha, ovos, leite)