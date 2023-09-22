#2 xícaras de farinha, 3 ovos, 5 colheres de leite
#A xícaras de farinha, B ovos, C colheres de leite em casa
#medida exata
import math
def bolos(a,b,c):
    """Calculo da quantidade máxima de bolos que João consegue fazer.
    a(xicara de f),b(ovos),c(colheres de leite)"""
    return math.floor(min(a/2,b/3,c/5))