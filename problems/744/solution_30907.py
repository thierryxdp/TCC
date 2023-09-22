from math import floor
def hashtag(s):
    #Essa função passa uma string, em que terá as # no inicio, meio e fim.
    # str-> str
    meioFrase = floor(len(s) / 2)
    return '#' + s[:meioFrase] + '#' + s[meioFrase:] + '#'