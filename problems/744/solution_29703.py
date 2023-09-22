# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    contagem = len(s)
    divisao = contagem / 2
    return str('#') + s[0:divisao] + str('#') + s[divisao + 1:] + str('#')