def hashtag(s):
    '''Função que tem como entrada uma string e retorna essa mesma string com
    uma 'hashtag' no início, meio e fim dessa string.
    str -> str'''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'