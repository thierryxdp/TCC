from math import *
#Exercício 3 - OBI: quantos bolos João pode fazer
def bolos(a : int, b : int, c : int) -> int:
    '''A função recebe, respectivamente, a quantidade de xícaras de farinha de
        trigo (a), de ovos(b) e de colheres de sopa de leite o usuário tem em
        casa e divide pela quantidade necessária para fazer uma receita e
        retorna o valor total de bolos que podem ser feitos com aquela
        quantidade de ingredientes. Nenhum dos argumentos pode receber valores
        negativos, se receberem a função não funcionará corretamente.'''
    '''x = a//2
    y = b//3
    z = c//5
    
    if(x<y and x<z):
        return x
    elif (y<z):
        return y
    else:
        return z'''
    return min(a//2,b//3,c//5)