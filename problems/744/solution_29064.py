def hashtag(s):
    """Função que adiciona # no inicio, meio e fim de uma string.Ex.: abcd -> #ab#cb#"""
    return '#'+s[:int(min(len(s)/2))]+'#'+s[int(min(len(s)/2)):]+'#'