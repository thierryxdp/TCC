def bolos(xicaras=2, ovos=3, colheres=5)=1:
    '''Essa funcao calcula a quantidade maxima de bolos que Joao consegue fazer, dado o numero de xicaras de farinha de trigo, de ovos, e de colheres de sopa de leite.'''
    return min(xicaras, ovos, colheres)