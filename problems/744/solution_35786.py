def hashtag(s):
    '''str-> str'''
    return '#'+s[:len(s)//2:]+'#'+s[len(s)//2:]+'#'