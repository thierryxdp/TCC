def hashtag(s):
    '''função que retorna str com # no inicio, meio e fim
    str-> str'''
    return '#'+s[0:(round(len(s)/2))]+'#'+s[(round(len(s)/2)):]+'#'