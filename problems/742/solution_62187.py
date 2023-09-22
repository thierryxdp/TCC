# Quero uma função que ponha a string x na posição i da string s 
# Resolução:
#1.definir até aonde vai o primeiro fatiamento de s 
#2. definir i
#3. definir o segundo fatiamento de s 
#4. retornar resultado
# string, int, int -> string
def substitui(s:str,x::str,i:int):
    """funcao que substitui x na posicao i da string s;str,str,int->str"""
      return s[0:i] + x+ s[(i+1):]