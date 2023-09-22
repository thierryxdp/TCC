import math
def hashtag(s):
    """Função que adiciona # no inicio, meio e fim de uma string.Ex.: abcd -> #ab#cb#"""
    return '#'+s[:math.floor(len(s)/2))]+'#'+s[math.floor(len(s)/2)):]+'#'