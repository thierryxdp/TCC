def hashtag(s):
    '''str -> str'''
    return '#'+str.partition(s,'#')+'#'