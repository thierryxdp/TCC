def hashtag(s):
    '''Essa função retorna uma string dividida por hashtag no início, meio e fim, str -> str'''
    s1=s[len(s)//2]
    s2=s[len(s)//2:]
    return '#'+s1+'#'+s2+'#'