# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   """Dado uma palvra retorna com o hashtag na frente, no meio e no final.string>string"""
   mid=len(s)//2
   return "#"+ s[:mid]+"#"+ s[mid:]+"#"