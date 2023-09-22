def hashtag(s):
    """funcao que recebe um string e insere '#'
    no inicio,meio e final dessa string; str -> str"""
    x = len(s)//2
    return '#'+str(s[:x])+'#'+str(s[x:])+'#'