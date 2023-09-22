# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'função que insere caracter em 3 posições de uma string.'
    meio = len(s) // 2
    return '#'+s[0:meio]+'#'+s[meio:len(s)]+'#'