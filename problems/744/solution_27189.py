# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   meio = len(s)
   a = int(meio/2)
   return '#'+ s[0:a]+ '#'+s[a:]+'#'