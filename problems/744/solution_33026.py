# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   lucas = len(s)
   inteiro = lucas / 2
   a = s[:(inteiro):]
   
   b = s [(inteiro+1)::]       
   
   c = '#'
   return c + a + c + b + c