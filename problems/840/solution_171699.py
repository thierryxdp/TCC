def bolos(a,b,c):
    '''Calcula e retorna o a quantidade de bolos que pode ser feita com a xícaras de farinha, b ovos e c colheres de leite.
    int,int=>float'''
    return min((a//2),(b//3),(c//5))