from math import *
def bolos(A,B,C):
    farinha=floor(A/2)
    ovos=floor(B/3)
    leite=floor(C/5)
	return min(farinha,ovos,leite)