import math
def bolos (a,b,c):
	'''calcula quantos bolos são possiveis fazer dependendo da quantidade dos ingrediente'''
    trigo=a/2
    ovos=b/3
    leite=c/5
    return math min(trigo,ovos,leite)