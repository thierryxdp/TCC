def hashtag(s):
    '''função que recebe uma string e retorna a mesma string com '#' no início, meio e fim'''
    return '#'+s[:len(s)//2:]+'#'+s[len(s)//2:]+'#'