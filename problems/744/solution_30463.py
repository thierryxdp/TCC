# Coloca hastag no início, meio e fim de um texto
# str-> str
def hashtag(s):
    return '#' + s[0: s // 2] + s[s // 2 + 1:] + '#'