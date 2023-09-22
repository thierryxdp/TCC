# str-> str
def hashtag(s):
    nome = len(s)
    media = nome//2
    return '#' + s [ :media] + '#' + s[media: ] + '#'