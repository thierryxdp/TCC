# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
      """Dado uma palavra, essa função colocará uma
hashtag no inicio, no meio e ao fim da palavra"""
      x=len(s)
      y= x//2
      a = s[0:y]+'#'+s[y: ]
      return '#'+a+'#'