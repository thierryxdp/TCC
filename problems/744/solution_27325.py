# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'Dada uma string, retorna uma string com o caractere "#" no início, no meio e no final da mesma.'
    'str->str'
    return '#'+s[0:len(s)//2]+'#'+s[len(s)2//s:]+'#'