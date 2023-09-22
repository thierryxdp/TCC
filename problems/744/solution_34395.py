# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    t= len(s)
    return '#' + s[:int(t/2)] + '#' + s[int(t/2):] + '#'