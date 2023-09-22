# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que, dada uma string s, coloca o caracter '#' no início,
    no meio e no final dessa string.'''
    '''str->str'''
    return '#'+str(s)[0:len(str(s))//2]+'#'+str(s)[len(str(s))//2:len(str(s))]+'#'