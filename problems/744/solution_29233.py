def hashtag(s):
    """essa funçao retorna uma string com # no inicio, no meio e no final dela"""
    """entrada: str"""
    """saida: str"""
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'