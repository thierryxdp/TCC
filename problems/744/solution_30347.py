def hashtag(s):
    ''' str->str'''
    return '#'+s[0:/2]+'#'+s[/2:]+'#'