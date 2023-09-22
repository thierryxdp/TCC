bolos(a,b,c):
    '''Calcula a quatidade de bolos que João pode fazer com a xícaras de farinha, b ovos e c colheres de leite
    int,int=>int'''
    return min((a/2),(b/3),(c/5))