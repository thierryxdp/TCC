"""Retorna # no inicio, no meio e no final da palavra:
# str-> str"""

def hashtag(s):
    return '#'+s[:len(s)%2]+'#'+s[len(s)%2:]+'#'