def hashtag(s):
    '''retorna a string com o caractere "#" no inicio, meio e fim da string'''
    return '#'+str(s[0:len(s)//2])+'#'+str(s[len(s)//2:])+'#'