# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retornar a string de entrada s, com o caractere # inserido no início, meio e fim da string'''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'