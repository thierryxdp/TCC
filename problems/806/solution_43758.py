from math import *

def bolos (A,B,C):
    '''
    Calcula a quantidade máxima de bolos que João consegue fazer

    Uso (A,B,C)

    Entrada:
    - A (int, obrigatório): número de xícaras de farinha de trigo
    - B (int, obrigatório): número de ovos
    - C (int, obrigatório): número de colheres de sopa de leite

    Saída:
    - Quantidade bolos que João pode realizar (int)
    '''
    if A//2 >= 1:
        if B//3 >= 1:
            if C//5 >= 1:
                return min((A//2), (B//3) , (C//5))
    if A//2 <= 0:
        return (0)
    if B//3 <= 0:
        return (0)
    if C//5 <= 0:
        return (0)#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado