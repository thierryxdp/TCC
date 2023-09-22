"""Retorna # no inicio, no meio e no final da palavra:
# str-> str"""
antes = s[:len(s)%2]
depois= s[len(s)%2:]
s = '#'+antes+'s'+depois+'#'
def hashtag(s):
    return s