"""Função que recebe uma string e insere o caractere # no início, no meio e no final dela
str-> str"""
def hashtag(s):
    return '#'+ s[:(len(s)//2)] + '#' + s[(len(s)//2):] + '#'