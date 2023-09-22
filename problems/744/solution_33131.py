def hashtag(s):
    """Recebe uma palavra e devolve ela com # no inicio, no meio e no fim da palavra inserida;
    str -> str"""
    meio=len(s)//2
    return '#'+s[:meio]+'#'+s[meio+1:]+'#'