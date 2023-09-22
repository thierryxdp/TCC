import math

def bolos (A,B,C):
    '''função que calcula e retorna (em int), a quantidade máxima de
    bolos possível de se fazer com uma certa quantidade dos 
    ingredientes A,B,C (todos em int)'''
	a= (A//2)
    b= (B//3)
    c= (C//5)
    return min(a,b,c)