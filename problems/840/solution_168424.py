def bolos(a,b,c):
    '''Retorna o número de bolos, de uma determinada receita, que é possível fazer,
       dados: a quantidade de xícaras de farinha de trigo, o número de ovos, e a
       quantidade de colheres de sopa de leite'''
    '''int,int,int --> int'''
    nbolos = (a//2, b//3, c//5)
    return min(nbolos)