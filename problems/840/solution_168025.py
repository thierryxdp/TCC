#questão 3 bolos
def xicaras(A):
    '''Para saber quantos bolos João consegue fazer com as xícaras de farinha de trigo
    que tem é preciso resolver o cálculo ("A" é a quantidade de xícaras (precisa ser 
    um número inteiro, pois João quer medidas exatas)),(o cálculo vai dar a resposta 
    com um número inteiro, pois João quer medidas exatas)): A/2'''
    return int(A)//2

def ovos(B):
    '''Para saber quantos bolos João consegue fazer com os ovos
    que tem é preciso resolver o cálculo ("B" é a quantidade de ovos (precisa ser 
    um número inteiro, pois João quer medidas exatas)),(o cálculo vai dar a resposta 
    com um número inteiro, pois João quer medidas exatas)): B/3'''
    return int(B)//3

def colheres(C):
    '''Para saber quantos bolos João consegue fazer com as colheres de sopa de leite
    que tem é preciso resolver o cálculo ("C" é a quantidade de colheres de sopa de leite (precisa ser 
    um número inteiro, pois João quer medidas exatas)),(o cálculo vai dar a resposta 
    com um número inteiro, pois João quer medidas exatas)): C/5'''
    return int(C)//5

def bolos(A,B,C):
    ''' Para saber quantos bolos João consegue fazer é preciso pegar o menor número
    das respostas das funções (xicaras,ovos,colheres) como resposta'''
    return min(xicaras(A),ovos(B),colheres(C))