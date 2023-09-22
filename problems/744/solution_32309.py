def hashtag(s):
    '''Esta função recebe uma string e retorna a mesma com um hashtag na frente.
    str-->str'''
    fim1=len(s)//2
    return '#'+s[0:fim1]+'#'+s[fim1:len(s)]+'#'