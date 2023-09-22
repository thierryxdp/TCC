'''funçao que recebe uma str e insere uma # no sei começo meio e fim. str->str'''
import math
def hashtag(s):
    """coloca # no inicio, meio e fim de uma string
     string->string"""
    meio = math.floor(len(s)/2)
    return '#' + s[:meio] + '#' + s[meio:] +'#'