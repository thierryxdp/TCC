# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dada uma string retorna ela com # no inicio, no meio e no final.'''
    metadeInt =len(s)//2
    resto= len(s)%2
    if (len(s) == 0):
        return '##'
    elif (len(s) == 1):
        return '#'+s+'#'
    else:
        return '#'+s[0:metadeInt]+'#'+s[metadeInt:]