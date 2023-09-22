def hashtag(s):
    """Função que adiciona # no inicio, meio e fim de uma string.Ex.: abcd -> #ab#cb#"""
   	x=(len(s))/2
    return '#'+s[:x]+'#'+s[x:]+'#'