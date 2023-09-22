def hashtag(s):
    """Ao inserir uma string nessa funcao, ela retornara a string dividida em partes e adicionando uma # no inicio, meio e fim
    :param s: str->str
    :return: str"""
 	meio=floor(len(s)/2)
 	return '#'+s[0:meio]+'#'+s[meio:]+'#'