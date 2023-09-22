def hashtag(s):
    """Função que adiciona # no inicio, meio e fim de uma string.Ex.: abcd -> #ab#cb#"""
    return '#'+s[:len(s)]+'#'+s[len(s):]+'#'