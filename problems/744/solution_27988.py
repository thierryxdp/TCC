def hashtag(s):
    '''função que recebe uma string e retorna a string com o caractere # no início, 
    meio e fim do parametro
    str->str'''
    return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'