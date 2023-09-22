def hashtag(s):
    '''funcao que inseri o # que retorna uma string dividida em parte no inicio, meio e fim
    :param s: str->str
    :return: str
    '''
    meio= floor(len(s)/2)
    return '#'+s[0:meio]+'#'+s[meio]+#