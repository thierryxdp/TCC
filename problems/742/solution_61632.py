# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(frase,letra,i):
    '''Entre com uma string, um caracter e um numero inteiro para retornar
    uma nova string com o caracter na posição do inteiro
    string, char, int -> string'''
	
    num=i//2
    frase2=frase.replace(frase[num], letra, 1)
  
    return frase2