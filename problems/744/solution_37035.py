#Função que coloca # no ínicio, meio e final de uma string. Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
      i=(len(str(s))//2)
    return '#'+s[0:i]+'#'+s[i:0]+'#'