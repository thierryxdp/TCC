def hashtag(s):
    '''Função que recebe uma string e adiciona uma # no inicio, meio e fim. 
    str -> str'''
    i=round((len(s)/2))
    return '#' + s + '#'+s[i::]+'#'