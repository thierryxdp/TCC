def hashtag(s):
    '''função que divide uma string no começo, meio e fim com o caractere #''' 
    ''' str->str''' 

    q = int(len(s)/2)
    return '#'+s[:q]+'#'+s[q:]+'#'