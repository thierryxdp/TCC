def hashtag(s):
    '''função que recebe uma string e insere o caractere '#' no início, no meio e no final dela;
       str -> str'''
        s = str(s)
        return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'