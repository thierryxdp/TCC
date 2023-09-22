import math
def bolos (A,B,C):
    '''Função que deve retornar o número máximo que 
    consegue fazer de bolo, sendo passado como parâmetro
    A(indicando número de xígaras de farinha de trigo),
    B(indicando o número de ovos) e C (indicando o número
    de colheres de sopa de leite);
    int,int,int -> int'''
    quantidade_de_bolo = min(A//2,B//3,C//5)
    return quantidade_de_bolo