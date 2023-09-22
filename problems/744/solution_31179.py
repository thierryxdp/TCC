# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "Coloca uma hashtag no início, meio e final da string 's'; str -> str"
    metade = len(s)//2
    return '#'+s[0:metade]+'#'+s[metade:]+'#'