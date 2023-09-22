def hashtag(s):
    '''coloca # no início, final e meio da string'''
    '''str-> str'''
    a = len(s)//2
    s = s.replace(s[a], '#'+s[a])
    s = '#'+s+'#'
    return s