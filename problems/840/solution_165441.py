from math import *
def bolos(A,B,C):
    """calcula e retorna o número máximo de bolos que João é capaz de fazer 
    dados A=número de xícaras de farinha de trigo, B=número de ovos e C= números
    de colheres de sopa de leite que ele tem disponíveis e sabendo que cada bolo
    consome 2 de A, 3 de B e 5 de C;
    int,int,int->int"""
    farinha=floor(A/2)
    ovos=floor(B/3)
    leite=floor(C/5)
	return min(farinha,ovos,leite)