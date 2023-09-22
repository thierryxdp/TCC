def substitui(s,x,i):
    '''Substitui determinado elemento, numa posição (i) de 
    uma string (s) por um caractere (x).
    string, int, int -> string'''
    return s[0:i]+x+s[(i+1): ]
def acima_da_media(lista):
    '''Função que retorna uma lista ordenada com as notas acima
    da média de uma determinada lista com notas dos alunos.'''
	return sum(lista)/len(lista)