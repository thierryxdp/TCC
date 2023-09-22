def bolos(a,b,c):
    '''Calcula a quantidade exata de bolos que podem ser preparados com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite.'''
    x = a/2
    y = b/3
    z = c/5
    return min(x,y,z)