# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s=str, x=int, i=int):
    s = str(input("escreva aqui a string")
    x = int(input("digite aqui o caracter")
    i = int(input("digite um número aqui")
    s[i] = x
	return s[0:i] + x + s[i + 1:]