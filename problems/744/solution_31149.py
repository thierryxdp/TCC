import math
def hashtag(s):
    """insere o caractere '#' no início, no meio e no final de uma string s dada"""
    """str->str"""
    return '#'+s[0:math.floor(len(s)/2)]+'#'+s[math.floor(len(s)/2):]+'#'