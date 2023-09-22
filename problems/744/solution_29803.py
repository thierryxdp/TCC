"""Criar uma funcao que receba uma string e tenha hashtag no inicio,meio e fim 
str-> str"""
def hashtag(s):
    return len(s)//2 ('#') + (s[0:s//2]) + ('#') + (s[s//2:]) + ('#')