def bolos(A,B,C):
'''função que calcula quantos bolos João consegue fazer'''
trigo= A//2
ovos= B//3
leite= C//5
return min (trigo,ovos,leite)