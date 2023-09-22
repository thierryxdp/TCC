# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,z1):
    '''Entre com uma string, um caracter e um numero inteiro para retornar
    uma nova string com o caracter na posição do inteiro
    string, char, int -> string'''
	
    m= s.replace(s[z1], x)
  
    return m