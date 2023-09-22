# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) == 8:
        return '#' + s[0:4] + '#' + s[4:] + '#'