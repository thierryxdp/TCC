def hashtag(s):
    '''Função que insere o caractere # no início, meio e fim de 
    uma string s. str->str'''
    x=len(s)//2
    return '#'+s[0:x]+'#'+s[x:]+'#'