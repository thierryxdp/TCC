# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funçao que insere o caractere (#) no inicio, no meio e no final dela'''
    '''3str->str'''
    if len(s)==0:
        return '#'+'#'+s+'#'
    if len(s)==1:
        return '#'+'#'+s+'#'
    if len(s)==2:
        return '#'+s[0:1]+'#'+s[1:2]+'#'
    if len(s)==3:
        return '#'+s[0:1]+'#'+s[1:3]+'#'
    if len(s)==4:
        return '#'+s[0:2]+'#'+s[2:4]+'#'
    if len(s)==5:
        return '#'+s[0:2]+'#'+s[2:5]+'#'
    if len(s)==6:
        return '#'+s[0:3]+'#'+s[3:6]+'#'
    if len(s)==7:
        return '#'+s[0:3]+'#'+s[3:7]+'#'
    if len(s)==8:
        return '#'+s[0:4]+'#'+s[4:8]+'#'
    if len(s)==9:
        return '#'+s[0:4]+'#'+s[4:9]+'#'
    if len(s)==10:
        return '#'+s[0:5]+'#'+s[5:10]+'#'
    if len(s)==11:
        return '#'+s[0:5]+'#'+s[5:11]+'#'
    if len(s)==12:
        return '#'+s[0:6]+'#'+s[6:12]+'#'
    if len(s)==14:
        return '#'+s[0:7]+'#'+s[7:14]+'#'