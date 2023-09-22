def hashtag(s):
    '''função que recebe uma string e insere o caractere '#' no início, no meio e no final dela;
       str -> str'''
    return '#'+str(s)[0:len(s)//2]+'#'+str(s)[len(s)//2:]+'#'