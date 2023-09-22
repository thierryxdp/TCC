# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)//2
    y=s[:x ]
    z=s[x :]
    return '#'+y+'#'+z+'#'