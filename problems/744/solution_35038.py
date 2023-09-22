def hashtag(s):
    '''função que insere # no início, meio e fim de uma string
    str->str'''
    x=len(s)//2
    return '#'+s[0,x]+'#'+s[x:]+'#'