# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    contagem = len(s)
    divisao = contagem / 2
    return '#' + s[0:divisao] + '#' + s[divisao + 1:] + '#'