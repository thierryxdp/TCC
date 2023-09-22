def hashtag(s):
    """retorna uma string s com # no começo, meio e fim dela"""
    """str -> str"""
    x = (len(s))//2
    if len(s)==1:
        return '#' + s + '#'
    else:
        return '#'+s[0:x]+ '#'+ s[x:] +'#'