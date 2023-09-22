# quero uma função que substitui x, na posição i da string s 
#resolução:
#1.definir o primeiro fatiamento de s
#2.definir x
#3.definir o segundo fatiamento de s 
#4.retornar resultado
# string, int, int -> string
def substitui(s,x,i):
  
          return s[0:i] + x+ s[(i+1):]