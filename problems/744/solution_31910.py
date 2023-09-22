# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   """retorna a string s com uma hashtag no inicio, no meio e
   no final.(str->str)"""
   x=((len(s))//2)
   str1=str("#")+s[0:(x+1)]+str("#")+s[(x+1):]+str("#")
   return str1