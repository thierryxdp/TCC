# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """dada ums trign, retorna a string com hashtags no inicio, 
    no meio e no fim da string. str->str"""
    metade = len(s)//2
    string = '#'+s[0:metade]+'#'+s[metade:]+'#'
    return string