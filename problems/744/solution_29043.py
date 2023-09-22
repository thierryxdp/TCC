"""Retorna # no inicio, no meio e no final da palavra:
# str-> str"""
s= s[:len(s)%2]+s+ s[len(s)%2:]
def hashtag(s):
    return s