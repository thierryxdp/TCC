def hashtag(s):
    """insere o caractere '#' no início, no meio e no final de uma string s dada"""
    """str->str"""
    return '#'+s[0:round(len(s)/2)]+'#'+s[round(len(s)/2):]+'#'