# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma str e insira # no meio str>str"""
   m = len(s)//2
   nova = '#'+s[0:m]+'#'+s[m:]+'#'
   return nova