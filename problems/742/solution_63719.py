# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s:str,x:str,i:int)->str:
   # essa funcao troca um caracter da string
s[i]=x
return s[0:(i-1)]+s[i]+s[i+1}