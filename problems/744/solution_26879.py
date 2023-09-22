# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe uma string e insere '#' no início, meio e fim do texto.
    str -> str'''
    x = (len(s))//2
    return '#'+s[0:x]+'#'+s[x:]+'#'