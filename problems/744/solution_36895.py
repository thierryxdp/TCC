# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = s.len()//2
    return '#'+s[:x]+"#"+s[x+1:]+'#'