# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que retorna a string s com # no início, no meio e no final dela.
    string->string'''
    tamanho=len(s)
    return '#'+s[:(tamanho//2)]+'#'+s[(tamanho//2):]+'#'