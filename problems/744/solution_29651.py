def hashtag(s):
    '''insere o caractere '#' no início, meio e fim da string s
    str -> str'''
    return '#'+s[0:(len(s)//2)]+'#'+s[((len(s)//2)+1):]+'#'