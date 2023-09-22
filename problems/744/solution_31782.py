# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) == 1:
     return str() + '#' + s + str() + '#'
    elif len(s) == 2:
     return str() + '#' + s[0:1] + str() + '#' + s[1:2] + str() + '#'
    elif len(s) == 3:
     return str() + '#' + s[0:1] + str() + '#' + s[1:3] + str() + '#'
    elif len(s) == 4:
     return str() + '#' + s[0:2] + str() + '#' + s[2:4] + str() + '#'
    elif len(s) == 5:
     return str() + '#' + s[0:2] + str() + '#' + s[2:5] + str() + '#'
    elif len(s) == 6:
     return str() + '#' + s[0:3] + str() + '#' + s[3:6] + str() + '#'
    elif len(s) == 7:
     return str() + '#' + s[0:3] + str() + '#' + s[3:7] + str() + '#'
    elif len(s) == 8:
     return str() + '#' + s[0:4] + str() + '#' + s[4:8] + str() + '#'