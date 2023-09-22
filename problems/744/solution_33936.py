def hashtag(s):
    '''Dada uma string s, retorna a mesma string com '#' no início, meio e fim dela
       str -> str'''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'