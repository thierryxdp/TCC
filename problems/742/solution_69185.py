# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma str igual a s, exceto que o elemento da posição i deve ser substituído por x
	Entrada: str,int.int
	Saída: str'''
    return s[:i]+ str(x) + s[i:]