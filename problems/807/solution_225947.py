from math import *
def conta_frases(t):
    '''Função que, dado um texto (t), determina
a quantidade de frases do mesmo;
str -> int'''
    return str.count(t,'.') + str.count(t,'!')+ str.count(t,'?') - 2 * str.count(t,'...')