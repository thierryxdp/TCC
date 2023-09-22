from math import ceil
def carros(p,c=5):
'''Calcula o número exato de carros necessários para uma viagem, dado 
   o valor p de pessoas e c de carros, que por definição será 5'''
return ceil(p/c)