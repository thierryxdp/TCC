def hashtag(s):
    '''Função que recebe uma string e adiciona uma # no inicio, meio e fim. 
    str -> str'''
    import math
    i=math.floor((len(s)/2))
    return '#' + s + '#'+s[i::]+'#'