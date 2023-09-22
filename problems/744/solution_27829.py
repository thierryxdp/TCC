def hashtag(s):
    '''dada uma string, retorna essa mesma string com o caractere '#' no inicio, meio e final dela;
    str --> str'''
    x = len(s)//2
    return '#'+s[:x]+'#'+s[x:]+'#'