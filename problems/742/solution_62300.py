# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
	'''Recebe uma tupla composta por uma String, um caractere e um número inteiro entre 0 e o comprimento da string, e retorna a string dada com o elemento de posição igual ao número inteiro dado substituido pelo caractere dado.'''
    troca=list(s)
    troca[i]=str(x)

    stringnova="".join(troca)

    return stringnova