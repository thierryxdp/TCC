def hashtag(s):
    '''funcao que inseri o # que retorna dividido em tres partes com inicio, meio e fim
    :param s: str->str
    :return: str
    '''
    meio =floot(len(s)/2)
    return '#'+s[:meio]+'s'[meio:]+'#'