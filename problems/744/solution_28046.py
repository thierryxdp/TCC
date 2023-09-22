def hashtag(s):
    '''retornar uma string com o # no início dela, no meio e no final.
    str-->str'''
    n=len(s)
    med=n//2
    return '#'+s[ :med]+'#'+s[med: ]+'#'