# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
#STRING ---- > STRING
 i = len(s)
 if i%2 == 0:
  return '#' +s[0:i//2] + '#' + s[i//2:]+ '#'
 else:
  return '#' + s[0:(i-1)//2]+ '#'+s[(i-1)//2:] + '#'