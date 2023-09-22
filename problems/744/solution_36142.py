def hashtag(s):
    """função que recebe uma string e inseri o caractere # no início,no meio e no final dela."""
    """ str->srt"""
    meio = len(s)//2
    return '#'+s[0:meio]+'#'+s[meio:]+'#'