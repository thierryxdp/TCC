# Coloca hastag no início, meio e fim de um texto
# str-> str
def hashtag(s):
    return '#' + s[0: len(s) // 2] + '#' + s[len(s) // 2 + 1:] + '#'