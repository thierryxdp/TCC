# Funcao concatenação
# entrada: 
# a = string
# b = string
# saida:
# string
# recebe duas strings a e b e retorna 
# abba

def concatenacao(a, b):
	return a+b+b+a
print("Teste da funcao Concatenacao")
x = concatenacao('12', '34')
print('12, ', '34, ', x)
x = concatenacao('1', '234')
print('1, ', '234, ', x)
x = concatenacao('12', '3')
print('12, ', '3, ', x)