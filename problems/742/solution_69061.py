def substitui(s,x,i):
	'''
    funcao que recebe uma string s,
    um caractere x e um numero inteiro
    i e retorna a mesmas string s, mas
    com o elemento da posicao i substituido por x
	string, int, int -> string
    '''
    return s[0:i]+ str(x) +s[i+1:]