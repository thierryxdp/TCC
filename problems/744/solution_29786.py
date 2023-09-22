"""Criar uma funcao que receba uma string e tenha hashtag no inicio,meio e fim 
str-> str"""
def hashtag(s):
    return str ('#')+(s[0:s//2])+('#')+(s[s//2])+('#')