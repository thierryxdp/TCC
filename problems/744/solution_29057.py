"""Retorna # no inicio, no meio e no final da palavra:
# str-> str"""

def hashtag(s):
    return '#'+[:len(s)%2]+'s'+s[len(s)%2:]+'#'