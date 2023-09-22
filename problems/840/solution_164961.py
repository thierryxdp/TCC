import math
def bolo(a,b,c):
    '''Calcula o numeros de bolos que podem ser feitos aparti da quantidade de ingredientes a,a quantidade de xicara de farinha, b, a quantidade de ovos e c, a quantidade de colheres de leite.
    float,int,int--> int
    return min(math.floor(a/2),math.floor(b/3),math.floor(c/5))