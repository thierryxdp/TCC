# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dada uma string s, a função retorna essa string, acrescida
    de uma hashtag no início, meio e final da string.
    string -> string'''
    return '#'+s[:len//2]+'#'+s[len//2:]+'#'