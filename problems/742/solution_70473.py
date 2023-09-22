# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um número
    inteiro i e retorna uma string igual a s, porém o elemento da 
    posição i substituído pelo caractere x.
    assinatura: string, int, int --> string'''
	if i == 0:
        return x + s[1:]
    if i == [len(s)]:
        return s[len(s)] + x
    if i == i>0:
        return s[0:i] + x + s[i+1:]