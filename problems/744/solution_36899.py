# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #essa função fará com que seja acrescentado # no início, meio e fim da string
    x = len(s)//2
    #estou contruindo um termo, no caso x, para denotar o meio da string
    return '#'+s[:x]+"#"+s[x:]+'#'