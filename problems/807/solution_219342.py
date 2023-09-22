from math import *
def conta_frases(t):
    '''funçao que, fornecido um texto (t), determina
a quantidade de frases do mesmo
str -> int'''
    return str.count(t,'.') + str.count(t,'!')
+ str.count(t,'?') - 2 * str.count(t,'...')