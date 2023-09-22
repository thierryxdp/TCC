def hashtag(s):
   '''retorna palavra string com  hastag no inicio, no meio e no final
str->str'''
   Meio = len(s)//2
   Parte1 = s[0:Meio]
   Parte2 = s[Meio:len(s)]
   return '#'+Parte1+'#'+Parte2+'#'