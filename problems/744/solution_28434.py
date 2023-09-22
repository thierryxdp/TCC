def hashtag(s):
    """Função que a partir de uma string, insere o caracter "#" no inicio, no meio e no final da string"""
    i = int(len(s)/2)
    return '#'+s[0:i]+'#'+s[i:]+'#'