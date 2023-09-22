# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) == 1:
        return '#' + s[0:0] + '#' + s[1:] + '#'
    if len(s) == 3:
        return '#' + s[0:1] + '#' + s[1:] + '#'
    if len (s) < 6:
        return '#' + s[0:2] + '#' + s[2:] + '#'
    if len (s) < 8:
        return '#' + s[0:3] + '#' + s[3:] + '#'
    if len (s) < 10:
        return '#' + s[0:4] + '#' + s[4:] + '#'
    if len (s) < 12:
        return '#' + s[0:5] + '#' + s[5:] + '#'
    if len (s) < 14:
        return '#' + s[0:6] + '#' + s[6:] + '#'
    if len (s) < 16:
        return '#' + s[0:7] + '#' + s[7:] + '#'
    if len (s) < 18:
        return '#' + s[0:8] + '#' + s[8:] + '#'
    if len (s) < 20:
        return '#' + s[0:9] + '#' + s[9:] + '#'