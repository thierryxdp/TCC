from math import floor

def hashtag(s):
    """
    Ao inserir uma string nessa função, ela retornará a string dividida em partes
    e adicionando uma # no início, meio e fim.
    """
    meio = floor(len(s) / 2)
    return '#' + s[0:meio] + '#' + s[meio:] + '#'