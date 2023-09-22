# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e retorna essa string com o caractere '#' no início, meio e fim dela
    str -> str'''
    if len(s)%2==0:
        return '#'+s[0:((len(s))/2)+1]+'#'+s[((len(s))/2)+1:]+'#'
    else:
        return '#'+s[0:((len(s))/2)+0.5]+'#'+s[((len(s))/2)+0.5:]+'#'