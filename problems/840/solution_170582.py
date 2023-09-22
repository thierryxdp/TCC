import math as m

def farinha(A):
    '''
    	Funcao que retorna o menor inteiro, dada a quantidade de 
        xicaras de farinha de trigo (A) e aplicando a proporcao 
        da receita do bolo.
        Parametro: (A) int.
        Return: int.
    '''
    return m.floor(A/2)

def ovos(B):
    '''
    	Funcao que retorna o menor inteiro, dada a quantidade de 
        ovos (B) e aplicando a proporcao da receita do bolo.
        Parametro: (B) int.
        Return: int.
    '''
    return m.floor(B/3)

def leite (C):
    '''
    	Funcao que retorna o menor inteiro, dada a quantidade de 
        colheres de sopa de leite (C) e aplicando a proporcao da 
        receita do bolo.
        Parametro: (C) int.
        Return: int.
    '''
    return m.floor(C/5)

def bolos (A,B,C):
    '''
    	Funcao que retorna o numero maximo de bolos que podem ser
        feitos, dadas as proporcoes entre farinha (A), ovos (B) e
        leite (C).
        Parametros: (A,B,C) int.
        A = numero de xicaras de farinha de trigo.
        B = numero de ovos.
        C = numero de colheres de sopa de leite.
        Return: int.
    '''
    return min(farinha(A),ovos(B),leite(C))