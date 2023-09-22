def hashtag(s):
    """ retotna a entrada escolhida mas com o caractere # no inicio, no meio e no final
    str -> str"""
    s=str(s)
    x=len(s)
    return '#'+s[0:x//2]+'#'+s[x//2:]+'#'