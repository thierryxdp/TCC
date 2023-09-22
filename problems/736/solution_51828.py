# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    concatenacao = a + b + b + a 
	print(concatenacao)
a = str(input('Primeiro para concatenar: '))
b = str(input('Segundo para concatenar: '))
concatenacao(a, b)