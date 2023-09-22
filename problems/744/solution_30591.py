from math import floor
def hashtag(s):
    """Insere uma # no inicio,no meio e no final de uma str
    """
    meio = floor(len(s) / 2)
    return '#' + s[0:meio] + '#' + s[meio:] + '#'