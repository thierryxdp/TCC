# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
 meio1=s[ :len(s)//2]
 meio2=s[len(s)//2: ]
 return'#'+meio1+'#'+ meio2+'#'