# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s:str,x:str,i:int)->str:
   # essa funcao troca um caracter da string
	s1=s[0:i]+str(x)+s[i+1:]
	return str(s1)