from math import *
"""Retorna a quantidade de frases que um texto possui dado um texto"""
def conta_frases(texto):
    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - 2 * str.count(texto,'...')