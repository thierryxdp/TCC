from math import *

def conta_frases(texto):
  """Retorna a quantidade de frases que um texto possui dado um texto"""
   return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - 2 * str.count(texto,'...')