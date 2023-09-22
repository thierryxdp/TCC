# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que inclui hashtah no começo, meio e fim das palavras'''
    return '#'+ s[0:]//2+'#'+s[0://2+1:]+'#'