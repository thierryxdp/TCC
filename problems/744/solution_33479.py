# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    nome = s
    return '#' + nome[0:len(s)/2] + nome[len(s)/2:] + '#'