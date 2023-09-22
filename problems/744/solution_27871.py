def hashtag(s):
    """funcao que adiciona # no inicio meio e final de uma string; str->str"""
    m=int(len(s))//2
    return '#'+s[:m]+'#'+s[m:]+'#'