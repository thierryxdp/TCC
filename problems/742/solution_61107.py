# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
   '''
   Entrada:
   		É fornecido uma string s um caracter x e o numero de elementos i ---> str, str,int
   Saída:
   		Retorna a strins s com o ultimo elemento substituido por x ---> str
   '''
	str1 = s
	return str1[0:i] + str(x)