# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return '#' + s[0:s//2] + '#' + s[s//2+1:len(s)] + '#'