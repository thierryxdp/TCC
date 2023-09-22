# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
 	'''Recebe uma string s, um caractere x, e um numero inteiro i representando a posição de troca. Retornando uma string igual a s,
 porém, o elemento da posição i na string original é substituido pelo caractere x
 str, str, int -> str'''
	string = str(s)
    y = string[0:(i)]
    z = string[(i):]
   	print (y+x+z)