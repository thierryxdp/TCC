def hashtag(s):
    '''str -> str'''
    return '#'+str.join('#',s[:4])+'#'