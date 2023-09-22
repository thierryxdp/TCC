# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''A funcao retorna uma string s com hashtags no comeco, meio e fim sendo que
para palavras com numero impar de caracteres a hashtag do meio vira deslocada para
a esquerda'''
    if len(s)%2==0:
        return '#'+s[0:int((len(s)/2))]+'#'+s[int((len(s)/2)):len(s)]+'#'
    else:
        return '#'+s[0:int((len(s)/2))]+'#'+s[int((len(s)/2)):len(s)]+'#'