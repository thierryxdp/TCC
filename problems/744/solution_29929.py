def hashtag(s):
    '''Funcao que, dada uma string, insere hashtags no inicio, meio e final dela; str -> str'''
    return '#'+s[0:len(s)//2]+'#'+s[(len(s)//2)+1:]+'#'