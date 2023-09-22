# Função coloca # em inicio, meio e final de uma string
# str-> str
def hashtag(s):
    i=(len(str(s))//2)
    return '#'+s[0:i]+'#'+s[i:]'#'