def hashtag(s):
    '''função que insere # no início, meio e fim de uma string
    str->str'''
    x=s[-1]/2
    y=s[-1]-0.5
    if x==int:
        return '#'+s[0:x]+'#'+s[(x+1):]+'#'
    else:
        return '#'+s[0:y]+'#'+s[(y+1):]+'#'