def hashtag(s):
    '''Retorna a string s com o caractere #
    no início, no meio e no final dela; str-> str'''
    return '#'+s[:(len(s)//2):]+'#'+[(len(s)//2)::]+'#'