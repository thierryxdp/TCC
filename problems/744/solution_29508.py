def hashtag(s):
    """retorna uma string s com # no começo, meio e fim dela"""
    """str -> str"""
    x = (len(s))//2
        return '#'+s[0:x]+ '#'+ s[x:] +'#'