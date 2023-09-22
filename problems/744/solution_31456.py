# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade = (len(s)//2)
    inicio = s[0:metade]
    final = s[(metade):]
    return '#'+inicio+'#'+final+'#'