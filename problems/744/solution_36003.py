import math as m
def hashtag(s):
   '''função que posiciona o caractere '#' no meio no inicio e no fim de uma string s
    entrada:str
    saída:str'''
           return '#'+s[:m.len(s)//2]+'#'+s[m.len(s)//2:]+'#'