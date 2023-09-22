def hashtag(s):
    '''str -> str'''
    return '#'+str.partition(str(s),'#')+'#'