# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorno da string s substituindo por x o que estiver na posiçao i;
    string, int, int -> string'''
    	return s[:len(2)] + "x" + s[len(2) + 1:]