import math
def bolos(a,b,c):
    '''funçao que calcula a quantidade de bolos que da pra fazer seguindo a receita exata dados a quantidade de ingredientes , a= xicaras de farinha, b=ovos, c=colheres de sopa '''
    return min(a//2,b//3,c//5)