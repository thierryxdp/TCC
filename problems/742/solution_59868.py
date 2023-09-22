# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da mesma.
    Retorna o elemento da posição i substituído pelo caractere x.'''
    sbs=len(s)//2
    	return s[0:i] + x + s[i+1:len(s)]