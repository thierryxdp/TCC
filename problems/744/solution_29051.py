def hashtag(s):
    """Função que adiciona # no inicio, meio e fim de uma string.Ex.: abcd -> #ab#cb#"""
   	x=len(s)
    return '#'+s[:x/2]+'#'+s[x/2:]+'#'