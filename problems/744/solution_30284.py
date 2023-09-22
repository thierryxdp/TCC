# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe uma string e insere o caractere ”#” no inicio,
    no meio e no final dela. 
    str->str'''
    tam=len(s)
    i=len//2
    return '#'+s[0:i]+'#'+s[i:]+'#'