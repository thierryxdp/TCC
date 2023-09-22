def hashtag(s):
    '''retorna a string com # no inicio,meio e fim'''
    '''str->str'''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'