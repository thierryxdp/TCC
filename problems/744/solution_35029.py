def hashtag(s):
    '''função que insere # no início, meio e fim de uma string
    str->str'''
    return '#'+s[0:len(s)//2]+'#'+s[(len(s)+1)//2]+'#'