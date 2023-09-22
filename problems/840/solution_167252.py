"""Para fazer o maior número de bolos
que João consegue com A xícaras de farinha
de trigo, B ovos e C colheres de sopa de
leite, é necessário dividir essas
quantidades pela necessária para fazer
uma receita do bolo. POrtanto, A/2, B/3 e C/5;
Atentar para o fato de que Jão só fará
medidas exatas: y<BOLOS<z, BOLOS == y,
sempre o maior inteiro menor que BOLOS"""

def bolos(A,B,C):
    import math
    a=math.floor(A/2)
    b=math.floor(B/3)
    c=math.floor(C/5)
    return min(a,b,c)